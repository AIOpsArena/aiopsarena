<template>
  <div class="AF__diff-setting">
    <header>
      <span O-B>network-delay</span>
    </header>
    <main>
      <div>
        <span O-B>latency</span>
        <el-input
          v-model="latency"
          size="mini"/>
        <span O-R>{{ $t('fault.example') }}:2000ms</span>
      </div>
      <div>
        <span O-B>correlation</span>
        <el-input-number
          v-model="correlation "
          :min="1"
          size="mini"/>
      </div>
      <div>
        <span O-B>jitter</span>
        <el-input
          v-model="jitter"
          size="mini"/>
        <span O-R>{{ $t('fault.example') }}:2000ms</span>
      </div>
      <div>
        <span O-B>targetapp</span>
        <el-select
          v-model="app"
          :popper-append-to-body="false"
          :placeholder="$t('placeholder.choose')"
          size="mini"
          @change="pods = []">
          <el-option
            v-for="item in appOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"/>
        </el-select>
      </div>
      <div
        v-if="app !== ''"
        pods>
        <span O-B>targetpods</span>
        <el-checkbox-group
          v-model="pods"
          size="mini">
          <el-checkbox
            v-for="p in (podsDict[app] === undefined ? 3 : podsDict[app])"
            :key="p"
            :label="app + '-' + (p - 1).toString()"
            border/>
        </el-checkbox-group>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      latency: '',
      correlation: 1,
      jitter: '',
      app: '',
      appOptions: [{
        value: 'cartservice',
        label: 'cartservice'
      }, {
        value: 'checkoutservice',
        label: 'checkoutservice'
      }, {
        value: 'currencyservice',
        label: 'currencyservice'
      }, {
        value: 'emailservice',
        label: 'emailservice'
      }, {
        value: 'frontend',
        label: 'frontend'
      }, {
        value: 'paymentservice',
        label: 'paymentservice'
      }, {
        value: 'productcatalogservice',
        label: 'productcatalogservice'
      }, {
        value: 'recommendationservice',
        label: 'recommendationservice'
      }, {
        value: 'redis-cart',
        label: 'redis-cart'
      }, {
        value: 'shippingservice',
        label: 'shippingservice'
      }],
      podsDict: {
        'redis-cart': 2
      },
      pods: []
    }
  },
  methods: {
    getData() {
      return {
        loss: this.loss,
        latency: this.latency,
        jitter: this.jitter,
        correlation: this.correlation,
        targetapp: this.app,
        targetpods: this.pods
      }
    }
  }
}
</script>

<style>

</style>
