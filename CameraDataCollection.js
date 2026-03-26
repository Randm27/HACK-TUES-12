;

async function startCamera(){
    try{
         const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        const video = document.getElementById("camera");
        video.srcObject = stream;
        } catch (err) {
        console.error("Camera access denied:", err);
    }
};

function captureFrame() {
  const video = document.getElementById("camera");
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  const jpegData = canvas.toDataURL("image/jpeg");

  return jpegData;
};

async function sendFrameToBackend() {
  const frame = captureFrame();

  await fetch("/analyze-frame", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: frame })
  });
};

startCamera();