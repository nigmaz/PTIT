document.addEventListener("DOMContentLoaded", function () {
  const temperatureElement = document.querySelectorAll("h2")[0];
  const humidityElement = document.querySelectorAll("h2")[1];
  const lightElement = document.querySelectorAll("h2")[2];
  const chartCanvas = document.getElementById("visit-sale-chart");

  const maxDataPoints = 10; // Số lượng dữ liệu tối đa hiển thị trên biểu đồ

  const data = {
    labels: [], // Thời gian hiển thị trên biểu đồ
    datasets: [
      {
        label: "Nhiệt độ",
        backgroundColor: "rgba(255, 99, 132, 0.7)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
        data: [], // Dữ liệu nhiệt độ
      },
      {
        label: "Độ ẩm",
        backgroundColor: "rgba(54, 162, 235, 0.7)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
        data: [], // Dữ liệu độ ẩm
      },
      {
        label: "Ánh sáng",
        backgroundColor: "rgba(255, 206, 86, 0.7)",
        borderColor: "rgba(255, 206, 86, 1)",
        borderWidth: 1,
        data: [], // Dữ liệu ánh sáng
      },
    ],
  };

  const chartConfig = {
    type: "bar",
    data: data,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  };

  const visitSaleChart = new Chart(chartCanvas, chartConfig);

  function getRandomTemperature() {
    return Math.floor(Math.random() * 51); // Ngẫu nhiên từ 0 đến 50
  }

  function getRandomHumidity() {
    return Math.floor(Math.random() * 101); // Ngẫu nhiên từ 0 đến 100
  }

  function getRandomLight() {
    return Math.floor(Math.random() * 101); // Ngẫu nhiên từ 0 đến 100
  }

  function updateData() {
    const randomTemperature = getRandomTemperature();
    const randomHumidity = getRandomHumidity();
    const randomLight = getRandomLight();

    temperatureElement.textContent = `${randomTemperature}°`;
    humidityElement.textContent = `${randomHumidity}%`;
    lightElement.textContent = `${randomLight} klux`;

    const currentTime = new Date().toLocaleTimeString(); // Lấy thời gian hiện tại

    // Thêm dữ liệu mới vào mảng dữ liệu và labels
    data.labels.push(currentTime);
    data.datasets[0].data.push(randomTemperature);
    data.datasets[1].data.push(randomHumidity);
    data.datasets[2].data.push(randomLight);

    // Xoá dữ liệu cũ nếu vượt quá số lượng dữ liệu tối đa
    if (data.labels.length > maxDataPoints) {
      data.labels.shift();
      data.datasets[0].data.shift();
      data.datasets[1].data.shift();
      data.datasets[2].data.shift();
    }

    // Cập nhật biểu đồ
    visitSaleChart.update();
  }

  updateData();
  setInterval(updateData, 600); // Cập nhật dữ liệu mỗi 1 phút
});
