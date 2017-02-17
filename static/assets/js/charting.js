var ctx = document.getElementById("myChart").getContext('2d');


// Generate checkbox for each value in JSON
$.each(dataset, function () {
    $("#checkboxelist").append($("<li>").text(this.label).prepend(
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
    labels: ["Honors", "Pass", "Foundation"],

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
                labels: ["Honors", "Pass", "Foundation"],
            datasets: newdata
          },
                      tooltipTemplate: "<%if (label){%><%=label %>: <%}%><%= value + ' %' %>"

        });
    });

// Set height of checkbox menu to equal the chart
$(document).ready(function() {
  $("#checkboxes").css("height", $("#myChart").height());
});

