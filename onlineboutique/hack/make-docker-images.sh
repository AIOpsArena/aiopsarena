#!/usr/bin/env bash

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Builds and pushes docker image for each demo microservice.

set -euo pipefail
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

log() { echo "$1" >&2; }

APM_IP=$(kubectl get service apm-server-apm-server -n observe -o jsonpath="{.spec.clusterIP}")
TAG=0.0.2
REPO_PREFIX=wjjdoraemon

TAG="${TAG:?TAG env variable must be specified}"
REPO_PREFIX="${REPO_PREFIX:?REPO_PREFIX env variable must be specified}"

while IFS= read -d $'\0' -r dir; do
    # build image
    svcname="$(basename "${dir}")"
    builddir="${dir}"
    #PR 516 moved cartservice build artifacts one level down to src
    if [ $svcname == "cartservice" ] 
    then
        builddir="${dir}/src"
    fi
    if [[ $svcname == "adservice" || $svcname == "protos" ]] 
    then
        continue
    fi
    image="${REPO_PREFIX}/$svcname:$TAG"
    (
        cd "${builddir}"
        log "Building: ${image}"
        sed -i "s|ELASTIC_APM_SERVER_URL=.\+|ELASTIC_APM_SERVER_URL=http://${APM_IP}:8200|g" Dockerfile
        sed -i "s|OTEL_EXPORTER_OTLP_ENDPOINT=.\+|OTEL_EXPORTER_OTLP_ENDPOINT=http://${APM_IP}:8200|g" Dockerfile
        if [ -f appsettings.json ] ; then
            sed -i "s|\"ServerUrls\": \".\+\",|\"ServerUrls\": \"http://${APM_IP}:8200\",|g" appsettings.json
        fi
        if [ -f server.js ] ; then
            sed -i "s|serverUrl: '.\+'|serverUrl: 'http://${APM_IP}:8200'|g" server.js
        fi

        # docker build --pull -t "${image}" .

        docker build -t "${image}" . 
        log "Pushing: ${image}"
        docker push "${image}"

        # if [ $svcname != "frontend" ] && [ $svcname != "loadgenerator" ]
        # then
        #     log "Building: ${image}-native-grpc-probes"
        #     # docker build --pull -t "${image}-native-grpc-probes" . --target without-grpc-health-probe-bin
        #     docker build -t "${image}-native-grpc-probes" . --target without-grpc-health-probe-bin 
        #     log "Pushing: ${image}-native-grpc-probes"
        #     docker push "${image}-native-grpc-probes"
        # fi
    )
done < <(find "${SCRIPTDIR}/../src" -mindepth 1 -maxdepth 1 -type d -print0)

log "Successfully built and pushed all images."