var ctx = document.getElementById("myChart").getContext('2d');
// var dataset = [{
//       label: 'apples',
//       data: [12, 19, 3, 17, 28, 24, 7],
//       backgroundColor: "rgba(153,255,51,1)"
//     }, {
//       label: 'oranges',
//       data: [30, 29, 5, 5, 20, 3, 10],
//       backgroundColor: "rgba(255,153,0,1)"
//     },
//     {
//       label: 'bananas',
//       data: [30, 29, 5, 5, 20, 3, 10],
//       backgroundColor: "rgba(100,153,0,1)"
//     }]
// I need to be able to specify the columns being chosen
// I need the data in the format



// Generate checkbox for each value in JSON
$.each(dataset, function () {
    $("#checkboxes").append($("<label>").text(this.label).prepend(
        $("<input>").attr('type', 'checkbox').val(this.label)
           .prop('checked', this.checked)
    ));
});


// Find selected checkboxes
var selected = [];
$('#checkboxes input:checked').each(function() {
    selected.push($(this).attr('value'));
});


// Filter Data based on list
var newdata = $(dataset).filter(function(i,n){
    return selected.indexOf(n.label) > -1;
}).toArray();


// Generate chart
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    // labels: ["M", "T", "W", "T", "F", "S", "S"],
    labels: ["H", "G", "B"],

    datasets: dataset_start
  }
});


// Listen for the btnUpdate button click

    //    button click
    $("#btnUpdate").button().click(function(){
        // myChart.destroy();

        var selected = [];
        $('#checkboxes input:checked').each(function() {
            selected.push($(this).attr('value'));
        });

        // Filter Data based on list
        var newdata = $(dataset).filter(function(i,n){
            return selected.indexOf(n.label) > -1;
        }).toArray();

        // Destroy old chart
        //myChart.destroy();
        $('#myChart').remove(); // this is my <canvas> element
        $('#graph-container').append('<canvas id="myChart"><canvas>');
        ctx = document.getElementById("myChart").getContext('2d');

        // Generate chart
        var myChart =  new Chart(ctx, {
          type: 'bar',
          data: {
            // labels: ["M", "T", "W", "T", "F", "S", "S"],
                labels: ["H", "G", "B"],
            datasets: newdata
          },
                      tooltipTemplate: "<%if (label){%><%=label %>: <%}%><%= value + ' %' %>"

        });
    });
