var context
context=$("#context").val();
console.log(typeof(context));
context.replace(/&quot;/ig,'"');
console.log(context)
JSON.parse(context);
console.log(typeof(context));
console.log(context.intensity.averages.sector)

const ctx = document.getElementById('avg_intensity_sector');

// new Chart(ctx, {
//   type: 'bar',
//   data: {
//     labels: {{context.intensity.averages.sector.0|safe}},
//     datasets: [{
//       label: 'Average intensity by sector',
//       data: {{intensity.averages.sector.1|safe}},
//       borderWidth: 3
//     }]
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true
//       }
//     }
//   }
// });

// const ctx2 = document.getElementById('avg_intensity_region');

// new Chart(ctx2, {
//   type: 'bar',
//   data: {
//     labels: {{intensity.averages.region.0|safe}},
//     datasets: [{
//       label: 'Average intensity by region',
//       data: {{intensity.averages.region.1|safe}},
//       borderWidth: 3
//     }]
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true
//       }
//     }
//   }
// });

    

// const ctx3 = document.getElementById('avg_intensity_country');

// new Chart(ctx3, {
//     type: 'bar',
//     data: {
//     labels: {{intensity.averages.country.0|safe}},
//     datasets: [{
//         label: 'Average intensity by country',
//         data: {{intensity.averages.country.1|safe}},
//         borderWidth: 3
//     }]
//     },
//     options: {
//     scales: {
//         y: {
//         beginAtZero: true
//         }
//     }
//     }
// });