const vm = new Vue({
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
