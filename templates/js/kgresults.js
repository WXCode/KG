// JavaScript Document
//Width and height
    var req = new XMLHttpRequest()
    var jsonResponse;
    req.open('GET', this.window.location.origin + '/wrdvecs')
    req.onload = function () {
      jsonResponse = JSON.parse(req.responseText);
      var w = 500;
      var h = 500;
      var margin = { top: 20, right: 30, bottom: 30, left: 30 },
        width = w - margin.left - margin.right,
      height = h - margin.top - margin.bottom;

      var scaleX = d3.scaleLinear()
        .domain([d3.min(jsonResponse,function(d){return(d.GrLivArea)-20}), 
          d3.max(jsonResponse,function(d){return(d.GrLivArea)+20})])
        .range([0, 450]);
        var scaleY = d3.scaleLinear()
        .domain([d3.min(jsonResponse,function(d){return(d.SalePrice)-20}), 
          d3.max(jsonResponse,function(d){return(d.SalePrice)+20})])
        .range([0, 450]);


      // console.log(jsonResponse);
      //Create SVG element
      var svgcontainer = d3.select("#chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .call(d3.zoom().on("zoom",function(){
          svgcontainer.attr("transform",d3.event.transform)
        }));

      svgcontainer.append("g")
        .call(d3.axisLeft(scaleY));

      svgcontainer.append("g")
        .call(d3.axisRight(scaleY));

      svgcontainer.append("g")
        .call(d3.axisBottom(scaleX));

      svgcontainer.append("g")
        // .attr("transform", "translate(0," + height + ")")
        .call(d3.axisTop(scaleX));

      svgcontainer.append("g")
        .selectAll("circle")
        .data(jsonResponse)
        .enter()
        .append("circle")
        .attr("cx", function (d) {
          return (scaleX(d.GrLivArea));
        })
        .attr("cy", function (d) {
          return (scaleY(d.SalePrice));
        })
        .attr("r", 2.5)

      svgcontainer.append("g")
      .selectAll("text")
        .data(jsonResponse)
        .enter()
        .append("text")
        .text(function (d) {
          return (d.id);
        })
        .attr("x", function (d) {
          return (scaleX(d.GrLivArea)+4);
        })
        .attr("y", function (d) {
          return (scaleY(d.SalePrice)+4);
        })
        .attr("font-family","sans-serif")
        .attr("font-size","10px")
        .attr("fill","red")
    }

    req.send();
    console.log("request Sent");