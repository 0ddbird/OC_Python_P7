import * as d3 from 'd3';
export function displayGraph() {
    // Define functions
    const bruteForce = (n) => 1 + n * Math.pow(2, n) + Math.pow(2, n) + 1;
    const greedy = (n) => n * Math.log(n) + n;
    const dynamicProgramming = (n, capacity) => 2 * n * capacity + n;
    // Create a range of input values
    const inputData = d3.range(1, 101, 1);
    // Define constants for SVG
    const width = 800;
    const height = 500;
    const margin = { top: 20, right: 20, bottom: 50, left: 50 };
    // Create scales
    const xScale = d3.scaleLinear()
        .domain([0, d3.max(inputData)])
        .range([margin.left, width - margin.right]);
    // Use a logarithmic scale for the y-axis
    const yScale = d3.scaleLog()
        .base(2)
        .domain([1, d3.max(inputData.map((n) => bruteForce(n)))])
        .range([height - margin.bottom, margin.top]);
    // Create line generators
    const lineBruteForce = d3.line()
        .defined(d => !isNaN(d))
        .x((d, i) => xScale(i + 1))
        .y((d) => yScale(bruteForce(d)));
    const lineGreedy = d3.line()
        .defined(d => !isNaN(d))
        .x((d, i) => xScale(i + 1))
        .y((d) => yScale(greedy(d)));
    // For dynamic programming, we'll use a fixed capacity for demo
    const capacity = 10;
    const lineDynamicProgramming = d3.line()
        .defined(d => !isNaN(d))
        .x((d, i) => xScale(i + 1))
        .y((d) => yScale(dynamicProgramming(d, capacity)));
    // Create SVG
    const svg = d3.create("svg")
        .attr("viewBox", [0, 0, width, height]);
    // Add lines to the SVG
    svg.append("path")
        .datum(inputData)
        .attr("fill", "none")
        .attr("stroke", "red")
        .attr("d", d => lineBruteForce(d));
    svg.append("path")
        .datum(inputData)
        .attr("fill", "none")
        .attr("stroke", "green")
        .attr("d", d => lineGreedy(d));
    svg.append("path")
        .datum(inputData)
        .attr("fill", "none")
        .attr("stroke", "blue")
        .attr("d", d => lineDynamicProgramming(d));
    // Add axes
    const xAxis = (g) => g
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale).ticks(width / 80));
    const yAxis = (g) => g
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale));
    svg.append("g")
        .call(xAxis);
    svg.append("g")
        .call(yAxis);
    // Add the SVG to the body of the document
    const svgNode = svg.node();
    if (svgNode) {
        document.body.appendChild(svgNode);
    }
}
