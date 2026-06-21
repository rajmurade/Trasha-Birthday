"use client";

import React from "react";
import { Volume2, VolumeX } from "lucide-react";

interface AudioManagerProps {
  audioState: {
    isPlaying: boolean;
    toggle: () => void;
  };
}

export function AudioManager({ audioState }: AudioManagerProps) {
  const { isPlaying, toggle } = audioState;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex items-center gap-3">
      <span className="text-xs tracking-wider uppercase opacity-40 font-sans hidden sm:inline-block text-garden-text">
        {isPlaying ? "ambient melody playing" : "sound off"}
      </span>

      <button
        onClick={toggle}
        className="glass-button w-12 h-12 rounded-full flex items-center justify-center text-garden-accent hover:text-white transition-all focus:outline-none focus:ring-1 focus:ring-garden-glowPrimary"
        aria-label={isPlaying ? "Mute Background Music" : "Play Background Music"}
        title={isPlaying ? "Mute Music" : "Play Music"}
      >
        {isPlaying ? (
          <div className="relative flex items-center justify-center">
            <span className="absolute inline-flex h-full w-full rounded-full bg-garden-glowSecondary/30 animate-ping" />
            <Volume2 className="w-5 h-5 relative z-10" />
          </div>
        ) : (
          <VolumeX className="w-5 h-5" />
        )}
      </button>
    </div>
  );
}