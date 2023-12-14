document.addEventListener("DOMContentLoaded", function () {
    var playButton = document.getElementById("playButton");
    var videoOverlay = document.getElementById("videoOverlay");
    var videoFrame = document.getElementById("videoFrame");
    var closeButton = document.getElementById("closeButton");

    playButton.addEventListener("click", function () {
        var trailerId = playButton.getAttribute("data-trailer-id");
        if (trailerId) {
            videoFrame.src = "https://www.youtube.com/embed/" + trailerId;
            videoOverlay.style.display = "flex";
        }
    });

    closeButton.addEventListener("click", function () {
        videoFrame.src = "";
        videoOverlay.style.display = "none";
    });
});

window.onload = function () {
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    var x = canvas.width / 2;
    var y = canvas.height / 2;
    var radiusBackground = 35; // Raio da cor de fundo
    var radiusForeground = 25;  // Raio do círculo de porcentagem
    var endPercent = parseFloat(document.getElementById('nota').innerHTML) * 10;
    var curPerc = 0;
    var counterClockwise = false;
    var circ = Math.PI * 2;
    var quart = Math.PI / 2;

    context.lineWidth = 5;
   

    function getColor(percentage) {
        if (percentage <= 20) return '#FF0000'; // Vermelho forte
        if (percentage <= 40) return '#FFA500'; // Laranja
        if (percentage <= 60) return '#FFFF00'; // Amarelo
        if (percentage <= 80) return '#ADFF2F'; // Amarelo esverdeado
        return '#008000'; // Verde
    }

    function drawBackground() {
        context.beginPath();
        context.arc(x, y, radiusBackground, 0, circ, false);
        context.fillStyle = '#081c22';
        context.fill();
    }

    function drawSemi(){
        context.globalAlpha = 0.3;

        context.beginPath();
        context.strokeStyle = getColor(curPerc - 1);
        context.arc(x, y, radiusForeground, -(quart), circ - quart, false);
        context.stroke();
        
    }

    function animate(current) {
        context.clearRect(0, 0, canvas.width, canvas.height);

        drawBackground();
        drawSemi();
        context.globalAlpha = 1;
        context.beginPath();
        context.strokeStyle = getColor(curPerc - 1);
        context.arc(x, y, radiusForeground, -(quart), ((circ) * current) - quart, false);
        context.stroke();
        
        if (curPerc < endPercent) {
            curPerc++;
            requestAnimationFrame(function () {
                animate(curPerc / 100)
            });
        }
        
        context.fillStyle = 'white';
        context.font = '19px Arial';
        context.fillText((curPerc) + '%', x - 19, y + 7);
    }

    animate();
};