// @TODO: YOUR CODE HERE!

// set svg chart area
var svgWidth = 960;
var svgHeight = 500;

// set margins
var margin = {
    top: 20,
    right: 40,
    bottom: 100,
    left: 100
};

// set chart area with margins
var width = svgWidth - (margin.left + margin.right);
var height = svgHeight - (margin.top + margin.bottom);

// create SVG wrapper at HTML id scatter
// append SVG group with will hold our chart
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// shift chart by left and top margins
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

function makeAxis(x,y) {

console.log(x,y);

    // import data
    d3.csv("assets/data/data.csv").then(function(data) {
        // check data console log
        console.log(data);

        // step 1: parse data and cast as numbers
        
        data.forEach(d=>{
            // Healthcare vs. Poverty
            d.healthcare = +d.healthcare;
            d.income = +d.income;
            d.poverty = +d.poverty;
            // Smokers vs Age
            d.smokes = +d.smokes;
            d.age = +d.age;
            //console.log(d.age);
        })

        console.log(d3.extent(data, d=> d[x]));
        // [4.6, 24.9]
        console.log(d3.extent(data, d=> d[y]));
        // [9.2, 21.5]

        // step 2: Create scale functions

        var xScale = d3.scaleLinear()
            .domain([0.9*(d3.min(data,d=>d[x])),(d3.max(data,d=>d[x]))*1.1])
            .range([0,width]);
        
        var yScale = d3.scaleLinear()
            .domain([0.9*(d3.min(data, d=>d[y])),(d3.max(data, d=>d[y]))*1.1])
            .range([height,0]);
        
        // Step 3: Create axis functions
        var xAxis = d3.axisBottom(xScale);
        var yAxis = d3.axisLeft(yScale);
        
        // Step 4: Append Axes to the chart
        chartGroup.append("g")
            .attr("transform",`translate(0,${height})`)
            .call(xAxis);
        
        chartGroup.append("g")
            .call(yAxis);
        
        // step 5: create circles
        var circlesGroup = chartGroup.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => xScale(d[x]))
            .attr("cy", d => yScale(d[y]))
            .attr("r", "10")
            .attr("fill", "blue")
            .attr("opacity", ".3");
    
        
        /* Create the text for each block */
        var text = chartGroup.selectAll("text")
            .data(data)
            .enter()
            .append("text")
            .text(d=> d.abbr)
            .attr("x", d => xScale(d[x])-8)
            .attr("y", d => yScale(d[y])+5)
            .attr("font_family", "sans-serif")  // Font type
            .attr("font-size", "10px")  // Font size
            .attr("fill", "black");   // Font color;


        // Step 6: Initialize tool tip
        var toolTip = d3.tip()
            .attr("class", "d3-tip")
            .html(d=> {
                return (`${xText}: ${d[x]}<br>${yText}: ${d[y]}<br>State: ${d.abbr}`)
            });
        
        // step 7: Create tooltip in chart
        chartGroup.call(toolTip);

        // step 8: create event listener to display tooltip
        circlesGroup.on("mouseover", function(data) {
            toolTip.show(data, this);
        })
        // hide when mouseout
        .on("mouseout",function(data,index) {
            toolTip.hide(data);
        })
        
        // step 9: create axes labels
        // x-axis group

        let xlabelGrp = chartGroup.append("g")
        
        //healthcare
        let xHealthcare = xlabelGrp.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left + 40)
            .attr("x", 0 - (height / 1.5))
            .attr("dy", "1em")
            .attr("class", "axisText")
            .text(`Lacks Healthcare (%)`);

        let xSmokes = xlabelGrp.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left)
            .attr("x", 0 - (height / 1.5))
            .attr("dy", "1em")
            .attr("class", "axisText")
            .text(`Smokes (%)`);

        // y-axis 
        // poverty
        var poverty = chartGroup.append("text")
        .attr("transform", `translate(${width / 2.5}, ${height + margin.top + 30})`)
        .attr("class", "axisText")
        .text(`${yText}`);

        
    });
};

makeAxis("healthcare","poverty");

xSmokes.on("click", function(){
    makeAxis("smokes","poverty");
})