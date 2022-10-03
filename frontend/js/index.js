var backendUrl = 'http://127.0.0.1:5000';
var getskills = '/getskills';

// $(document).ready(function() {
//     $.ajax({ 
//         type: 'GET',
//         url: backendUrl + getskills,
//         crossDomain: true,
//         dataType: 'json',
//         success: function(responseData) {
//             console.log(responseData.data);
//             resdata = responseData.data.skill
//             console.log(resdata)
//             buildHtmlTable("#skill", resdata)
//         },
//         error: function(responseData, textStatus, errorThrown) {
//             alert('GET failed.');
//         }
//     })
// })

// Builds the HTML Table out of myList.
function buildHtmlTable(selector, myList) {
    var columns = addAllColumnHeaders(myList, selector);
  
    for (var i = 0; i < myList.length; i++) {
      var row$ = $('<tr/>');
      for (var colIndex = 0; colIndex < columns.length; colIndex++) {
        var cellValue = myList[i][columns[colIndex]];
        if (cellValue == null) cellValue = "";
        row$.append($('<td/>').html(cellValue));
      }
      $(selector).append(row$);
    }
  }
  
  // Adds a header row to the table and returns the set of columns.
  // Need to do union of keys from all records as some records may not contain
  // all records.
  function addAllColumnHeaders(myList, selector) {
    var columnSet = [];
    var headerTr$ = $('<tr/>');
  
    for (var i = 0; i < myList.length; i++) {
      var rowHash = myList[i];
      for (var key in rowHash) {
        if ($.inArray(key, columnSet) == -1) {
          columnSet.push(key);
          headerTr$.append($('<th/>').html(key));
        }
      }
    }
    $(selector).append(headerTr$);
  
    return columnSet;
  }