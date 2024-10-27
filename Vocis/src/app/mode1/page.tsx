"use client";

import { useState, useEffect, useRef } from "react";
import { Button } from "@/components/ui/button2";
import { Navbar } from "@/components/ui/Navbar";
import { Card } from "@/components/ui/card2";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function Page() {
  // State variables
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [timer, setTimer] = useState(0);
  const [isTimerRunning, setIsTimerRunning] = useState(false);
  const [generatedText, setGeneratedText] = useState("");
  const [mediaStream, setMediaStream] = useState<MediaStream | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [availableCameras, setAvailableCameras] = useState<MediaDeviceInfo[]>(
    []
  );
  const [selectedCameraId, setSelectedCameraId] = useState<string>("");

  // Refs for video element
  const videoRef = useRef<HTMLVideoElement>(null);

  // Effect to handle timer countdown
  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isTimerRunning && timer > 0) {
      interval = setInterval(() => {
        setTimer((prevTimer) => prevTimer - 1);
      }, 1000);
    } else if (timer === 0) {
      setIsTimerRunning(false);
    }
    return () => clearInterval(interval);
  }, [isTimerRunning, timer]);

  // Effect to fetch AI-generated text (simulated)
  useEffect(() => {
    const fetchGeneratedText = async () => {
      const response = await new Promise<string>((resolve) =>
        setTimeout(() => {
          resolve(
            "This is the AI-generated text.\n\nHere is another paragraph.\nAnd a new line here."
          );
        }, 1000)
      );
      setGeneratedText(response);
    };

    fetchGeneratedText();
  }, []);

  // Effect to enumerate available cameras
  useEffect(() => {
    const getCameras = async () => {
      try {
        const devices = await navigator.mediaDevices.enumerateDevices();
        const videoDevices = devices.filter(
          (device) => device.kind === "videoinput"
        );
        setAvailableCameras(videoDevices);
        if (videoDevices.length > 0) {
          setSelectedCameraId(videoDevices[0].deviceId);
        }
      } catch (err) {
        console.error("Error enumerating devices.", err);
        setError("Unable to access media devices.");
      }
    };

    getCameras();
  }, []);

  // Effect to access webcam and microphone based on selected camera
  useEffect(() => {
    const getMedia = async () => {
      if (!selectedCameraId) return;

      // Stop any existing media tracks before starting new ones
      if (mediaStream) {
        mediaStream.getTracks().forEach((track) => track.stop());
      }

      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: { deviceId: { exact: selectedCameraId } },
          audio: true,
        });
        setMediaStream(stream);

        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error("Error accessing media devices.", err);
        setError("Unable to access webcam and/or microphone.");
      }
    };

    getMedia();

    // Cleanup on component unmount
    return () => {
      if (mediaStream) {
        mediaStream.getTracks().forEach((track) => track.stop());
      }
    };
  }, [selectedCameraId]);

  // Handlers
  const handleSpeakToggle = () => {
    setIsSpeaking(!isSpeaking);
    // Implement actual speech functionality here
  };

  const handleRestart = () => {
    // Implement restart functionality here
  };

  const handleTimerStart = () => {
    if (timer > 0) {
      setIsTimerRunning(true);
    }
  };

  const handleCameraChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCameraId(event.target.value);
  };

  const firstCardRef = useRef(null);

  return (
    <>
      <Navbar />
      <div className="container relative h-screen md:flex md:flex-row lg:grid lg:max-w-full lg:grid-cols-[3fr_1.5fr] lg:px-0">
        {/* Sidebar Section */}
        <div className="relative hidden h-full flex-col bg-muted p-6 text-white dark:border-r lg:flex">
          <div className="absolute inset-0 bg-zinc-900" />
          <div className="relative z-20 flex flex-col h-full">
            {/* Top Grid of Cards */}
            <div className="flex-grow grid grid-cols-3 gap-3 mb-3">
              {[...Array(9)].map((_, i) => (
                <Card
                  ref={i === 0 ? firstCardRef : null}
                  key={i}
                  className="bg-zinc-800 rounded-lg shadow-md aspect-video flex items-center justify-center"
                >
                  {i === 0 ? (
                    // Embed the webcam video in the first card
                    <>
                      {error ? (
                        <p className="text-red-500 text-xs">{error}</p>
                      ) : (
                        <video
                          ref={videoRef}
                          autoPlay
                          playsInline
                          muted
                          className="w-full h-full object-cover rounded-md"
                        ></video>
                      )}
                    </>
                  ) : (
                    // Other cards can have their own content or remain empty
                    <div className="bg-zinc-700 w-full h-full rounded-md"></div>
                  )}
                </Card>
              ))}
            </div>
            {/* Bottom Controls */}
            <div className="flex flex-col space-y-1">
              {/* Speak, Restart, Timer Controls */}
              <div className="flex space-x-1">
                <Button
                  variant={isSpeaking ? "destructive" : "outline"}
                  className="text-xs px-3 py-1 bg-zinc-900"
                  onClick={handleSpeakToggle}
                >
                  {isSpeaking ? "Stop Speaking" : "Speak"}
                </Button>
                <Button
                  variant="outline"
                  className="text-xs px-3 py-1 bg-zinc-900"
                  onClick={handleRestart}
                >
                  Restart
                </Button>
                <div className="flex gap-2">
                  <Input
                    type="number"
                    placeholder="Timer (min)"
                    className="text-xs px-3 py-1 w-28 text-zinc-900"
                    onChange={(e) =>
                      setTimer(parseInt(e.target.value) * 60 || 0)
                    }
                    disabled={isTimerRunning} // Disable input while timer is running
                  />
                  {!isTimerRunning ? (
                    <Button
                      onClick={handleTimerStart}
                      variant="outline"
                      disabled={timer === 0}
                      className="text-xs px-3 py-1 bg-zinc-900"
                    >
                      Start Timer
                    </Button>
                  ) : (
                    <Button
                      onClick={() => setIsTimerRunning(false)}
                      variant="outline"
                      className="text-xs px-3 py-1 bg-red-600"
                    >
                      Stop Timer
                    </Button>
                  )}
                </div>
              </div>
              {/* Camera Chooser */}
              <div className="flex flex-col space-y-1 mt-3">
                <Label htmlFor="cameraSelect" className="text-center text-lg">
                  Select Camera
                </Label>
                <select
                  id="cameraSelect"
                  value={selectedCameraId}
                  onChange={handleCameraChange}
                  className="text-xs px-3 py-1 bg-zinc-800 text-white rounded-md"
                >
                  {availableCameras.map((camera) => (
                    <option key={camera.deviceId} value={camera.deviceId}>
                      {camera.label || `Camera ${camera.deviceId}`}
                    </option>
                  ))}
                </select>
              </div>
              {/* Add Slides Section */}
              <div className="flex flex-col space-y-1 mt-3">
                <Label htmlFor="Slides" className="text-center text-lg">
                  Add Slides (.pdf, .txt, .pptx)
                </Label>
                <Input id="Slides" type="file" accept=".pdf, .txt, .pptx" />
              </div>
            </div>
          </div>
        </div>
        {/* Main Content Section */}
        <div className="lg:p-6 h-screen flex flex-col items-center justify-center bg-white">
          <div className="w-full max-w-md space-y-3">
            {generatedText && (
              <Card className="h-screen p-3 bg-gray-100">
                <textarea
                  className="w-full h-full p-2 border border-gray-300 rounded-md resize-none"
                  value={generatedText}
                  readOnly
                  style={{ whiteSpace: "pre-wrap" }} // Preserve whitespace and line breaks
                />
              </Card>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
