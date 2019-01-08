var app1 = new Vue({
  el: '#app-1',
  data: {
    results: []
  },
  mounted() {
    axios.get('/catalog/api').then(response => {
      this.results = response.data
    })
  }
});

var app2 = new Vue({
  el: '#app-2',
  data: {
    results: []
  },
  mounted() {
    axios.get('/catalog/api/2/items').then(response => {
      this.results = response.data
    })
  }
});


