const vm = new Vue({
  el: '#app-1',
  data: {
    results: []
  },
  mounted() {
    axios.get('/api/catalog').then(response => {
      this.results = response.data
    })
  }
});

/*var app2 = new Vue({
  el: '#app-2',
  data: {
    results: []
  },
  mounted() {
    axios.get('/api/items').then(response => {
      this.results = response.data
    })
  }
});*/
