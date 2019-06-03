// from data.js
var tableData = data;

// YOUR CODE HERE!

// Select html body to insert rows
var tbody = d3.select("tbody");

// Loop through data and append one table row for each sighting
function initialData(data) {
    tbody.text("");
    data.forEach(sighting => {
        var row=tbody.append("tr");
        Object.entries(sighting).forEach(([key,value]) => {
                var cell = tbody.append("td");
                cell.text(value);
        });
    });
};

// Display datas
initialData(tableData);


// Set Click button
var button = d3.select("#filter-btn");

// Set Text box
var text = d3.select("#datetime");

// When new datetime string is entered, filter the tableData

function handleChange(event) {
    // Prevents button from refreshing page
    d3.event.preventDefault();
    console.log(text.property("value"));

    // Filter data
    var newTable = tableData.filter(sighting=>sighting.datetime===text.property("value"));
    
    // Display new data
    initialData(newTable);
}

// Listen to events and run function
text.on("change", function(){
    button.on("click",handleChange);
});





