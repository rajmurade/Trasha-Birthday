"use client";

import { useEffect, useState, useRef, useCallback } from "react";
import { AmbientSynth } from "@/lib/synth";

export function useAudio() {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const synthRef = useRef<AmbientSynth | null>(null);
  const fadeIntervalRef = useRef<any>(null);

  useEffect(() => {
    const audio = new Audio("/audio/piano.mp3");
    audio.loop = true;
    audio.volume = 0;
    audioRef.current = audio;

    synthRef.current = new AmbientSynth();

    return () => {
      audio.pause();
      if (synthRef.current) synthRef.current.stop();
      if (fadeIntervalRef.current) clearInterval(fadeIntervalRef.current);
    };
  }, []);

  const fadeVolume = useCallback((targetVolume: number, duration: number, onComplete?: () => void) => {
    if (!audioRef.current) return;
    if (fadeIntervalRef.current) clearInterval(fadeIntervalRef.current);

    const steps = 20;
    const intervalTime = duration / steps;
    const currentVolume = audioRef.current.volume;
    const volumeStep = (targetVolume - currentVolume) / steps;

    let stepCount = 0;
    fadeIntervalRef.current = setInterval(() => {
      if (!audioRef.current) return;
      
      const newVolume = audioRef.current.volume + volumeStep;
      audioRef.current.volume = Math.max(0, Math.min(1, newVolume));
      stepCount++;

      if (stepCount >= steps) {
        audioRef.current.volume = targetVolume;
        clearInterval(fadeIntervalRef.current);
        if (onComplete) onComplete();
      }
    }, intervalTime);
  }, []);

  const play = useCallback(() => {
    if (!audioRef.current) return;

    audioRef.current.play()
      .then(() => {
        setIsPlaying(true);
        fadeVolume(0.5, 1200);
      })
      .catch(() => {
        if (synthRef.current) {
          synthRef.current.start();
          setIsPlaying(true);
        }
      });
  }, [fadeVolume]);

  const pause = useCallback(() => {
    if (!audioRef.current) return;
    
    fadeVolume(0, 1000, () => {
      if (audioRef.current) {
        audioRef.current.pause();
      }
      if (synthRef.current) {
        synthRef.current.stop();
      }
      setIsPlaying(false);
    });
  }, [fadeVolume]);

  const toggle = useCallback(() => {
    if (isPlaying) {
      pause();
    } else {
      play();
    }
  }, [isPlaying, play, pause]);

  return {
    isPlaying,
    toggle,
    play,
    pause,
  };
}