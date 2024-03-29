function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample

  d3.json(`/metadata/${sample}`).then(function(response){
      console.log(response);
  

    // Use d3 to select the panel with id of `#sample-metadata`

    var panel = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata

    panel.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    Object.entries(response).forEach(([key,value]) => {
      panel.append('h6').text(`${key} : ${value}`);
    })
  })

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}


// function buildCharts(sample) {

//   // @TODO: Use `d3.json` to fetch the sample data for the plots

//     // @TODO: Build a Bubble Chart using the sample data

//     // @TODO: Build a Pie Chart
//     // HINT: You will need to use slice() to grab the top 10 sample_values,
//     // otu_ids, and labels (10 each).
// }

function init() {
  // Grab a reference to the dropdown select element


  // Use the list of sample names to populate the select options


    // Use the first sample from the list to build the initial plots

}

// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected
//   //buildCharts(newSample);
//   buildMetadata(newSample);
// }

// // Initialize the dashboard
// init();
