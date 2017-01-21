/*  Preprocess timeline */
function preprocessTimeline (timelineArray) {
  var temp = [];
  var hashes = {};
  timelineArray.map(JSON.parse).forEach(function (element) {
    if (!hashes[element.properties.id]) {
      temp.push(element);
      hashes[element.properties.id] = 1;
    }
  });

  timelineArray = temp;
  // It's an array of Redis Strings
  return timelineArray
  .sort(function (a, b) {
    var date1 = new Date(a.properties.created_at);
    var date2 = new Date(b.properties.created_at);

    if (date1 > date2) return -1;
    else if (date1 < date2) return 1;
    else return 0;
  });
}

