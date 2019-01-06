const vm = new Vue({
  el: '#app',
  data: {
    categories: [
      {
        "id": 1, 
        "items": [
          {
            "cat_id": 1, 
            "desc": "The latest in comfort, style and cost!", 
            "id": 1, 
            "title": "Boots"
          }
        ], 
        "name": "Soccer"
      }, 
      {
        "id": 2, 
        "items": [
          {
            "cat_id": 2, 
            "desc": "As used in the NBA", 
            "id": 2, 
            "title": "Indoor ball"
          }, 
          {
            "cat_id": 2, 
            "desc": "Great for local pickup games", 
            "id": 3, 
            "title": "Outdoor ball"
          }, 
          {
            "cat_id": 2, 
            "desc": "The only net for that full swoosh sound", 
            "id": 4, 
            "title": "Net"
          }
        ], 
        "name": "Basketball"
      }, 
      {
        "id": 3, 
        "items": [
          {
            "cat_id": 3, 
            "desc": "What a beautiful piece of hickory", 
            "id": 5, 
            "title": "Bat"
          }, 
          {
            "cat_id": 3, 
            "desc": "Handmade - childrens fingers make for exquisite stitching", 
            "id": 6, 
            "title": "Ball"
          }
        ], 
        "name": "Baseball"
      }, 
      {
        "id": 4, 
        "items": [
          {
            "cat_id": 4, 
            "desc": "Well...duh!", 
            "id": 7, 
            "title": "Frisbee"
          }
        ], 
        "name": "Frisbee"
      },
      {
        "id": 5, 
        "items": [
          {
            "cat_id": 5, 
            "desc": "Boutique board made from carbon fibre, the optimum mix of light-weight strength and profit margin", 
            "id": 8, 
            "title": "Snowboard"
          }, 
          {
            "cat_id": 5, 
            "desc": "Wrap around UV protection so you can see when you are being ripped off", 
            "id": 9, 
            "title": "Goggles"
          }, 
          {
            "cat_id": 5, 
            "desc": "Microfibre lining for warmth and stuff", 
            "id": 10, 
            "title": "Gloves"
          }
        ], 
        "name": "Snowboarding"
      }, 
      {
        "id": 6, 
        "items": [
          {
            "cat_id": 6, 
            "desc": "Supports a climber up to 200kgs (as long as their fingers do)", 
            "id": 11, 
            "title": "Rope"
          }, 
          {
            "cat_id": 6, 
            "desc": "Do we really sell these???", 
            "id": 12, 
            "title": "Rocks"
          }
        ], 
        "name": "Rock Climbing"
      }, 
      {
        "id": 7, 
        "items": [
          {
            "cat_id": 7, 
            "desc": "The good old pigskin", 
            "id": 13, 
            "title": "Football"
          }, 
          {
            "cat_id": 7, 
            "desc": "Best worn before your time in the concussion protocol", 
            "id": 14, 
            "title": "Helmet"
          }, 
          {
            "cat_id": 7, 
            "desc": "Bigger than those in an 80s sitcom", 
            "id": 15, 
            "title": "Shoulder pads"
          }
        ], 
        "name": "Football"
      }, 
      {
        "id": 8, 
        "items": [
          {
            "cat_id": 8, 
            "desc": "Almost obligatory", 
            "id": 16, 
            "title": "Surfboard"
          }
        ], 
        "name": "Surfing"
      }, 
      {
        "id": 9, 
        "items": [
          {
            "cat_id": 9, 
            "desc": "Field or ice?", 
            "id": 17, 
            "title": "Stick"
          }, 
          {
            "cat_id": 9, 
            "desc": "Well that explains the stick type", 
            "id": 18, 
            "title": "Ice Skates"
          }
        ], 
        "name": "Hockey"
      }
    ]
  }
});