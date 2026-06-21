"use client";

import React, { useEffect, useRef, useState } from "react";
import gsap from "gsap";
import { Sparkles } from "lucide-react";

interface BloomControllerProps {
  isActive: boolean;
  onTimelineProgress: (progress: number) => void;
  onComplete: () => void;
}

export function BloomController({ isActive, onTimelineProgress, onComplete }: BloomControllerProps) {
  const overlayRef = useRef<HTMLDivElement>(null);
  const textRef = useRef<HTMLDivElement>(null);
  const flashRef = useRef<HTMLDivElement>(null);

  const [stageText, setStageText] = useState("");

  // Use refs to store the callbacks so we don't restart the GSAP timeline when React re-renders the page
  const onTimelineProgressRef = useRef(onTimelineProgress);
  const onCompleteRef = useRef(onComplete);

  useEffect(() => {
    onTimelineProgressRef.current = onTimelineProgress;
    onCompleteRef.current = onComplete;
  }, [onTimelineProgress, onComplete]);

  useEffect(() => {
    if (!isActive) return;

    // Create pristine timeline
    const tl = gsap.timeline({
      onComplete: () => {
        if (onCompleteRef.current) {
          onCompleteRef.current();
        }
      },
    });

    const bloomObj = { progress: 0 };

    // 1. Initial dark cinematic fade
    tl.to(overlayRef.current, {
      opacity: 0.95,
      duration: 1.5,
      ease: "power2.out",
      onStart: () => setStageText("The garden fades as the stars align..."),
    });

    // 2. Glow energy builds up from roots
    tl.to(overlayRef.current, {
      backgroundColor: "#11071c",
      duration: 1.2,
      ease: "power1.inOut",
      onStart: () => setStageText("A quiet energy gathers at the stem..."),
    });

    // 3. Flower blooming (triggers state callback via ref)
    tl.to(bloomObj, {
      progress: 1,
      duration: 3.2,
      ease: "power2.inOut",
      onUpdate: () => {
        if (onTimelineProgressRef.current) {
          onTimelineProgressRef.current(bloomObj.progress);
        }
        if (bloomObj.progress > 0.2 && bloomObj.progress < 0.7) {
          setStageText("The translucent glass petals slowly unfold...");
        } else if (bloomObj.progress >= 0.7) {
          setStageText("The core begins to crystallize into light...");
        }
      },
    });

    // 4. Glow Flash transition
    tl.to(flashRef.current, {
      opacity: 1,
      duration: 0.3,
      ease: "power3.out",
      onStart: () => setStageText("A magic emerges..."),
    });

    tl.to(flashRef.current, {
      opacity: 0,
      duration: 0.8,
      ease: "power2.in",
    });

    // Elegant pause
    tl.to({}, { duration: 0.8 });

    return () => {
      tl.kill();
    };
  }, [isActive]); // Only trigger when isActive transitions to true

  if (!isActive) return null;

  return (
    <div className="fixed inset-0 z-40 pointer-events-none overflow-hidden flex flex-col items-center justify-center">
      {/* Dark Ambient overlay */}
      <div
        ref={overlayRef}
        className="absolute inset-0 bg-[#020206] opacity-0 transition-all duration-300 pointer-events-auto"
      />

      {/* Extreme white/pink flash screen */}
      <div
        ref={flashRef}
        className="absolute inset-0 bg-gradient-to-tr from-[#fff0f5] via-[#ffd6e7] to-white opacity-0 mix-blend-overlay pointer-events-none"
      />

      {/* Cinematic subtitle status */}
      <div
        ref={textRef}
        className="absolute bottom-28 left-1/2 -translate-x-1/2 text-center flex flex-col items-center gap-2 pointer-events-none"
      >
        <Sparkles className="w-5 h-5 text-garden-glowPrimary animate-pulse mb-1" />
        <p className="text-sm font-serif italic text-garden-glowPrimary/90 tracking-widest text-shadow">
          {stageText}
        </p>
      </div>
    </div>
  );
}