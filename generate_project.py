import os
import sys
from pathlib import Path
import zipfile

# Initialize the files dictionary
FILES_MAP = {}

# ----------------------------------------------------
# 1. package.json
# ----------------------------------------------------
FILES_MAP["package.json"] = """{
  "name": "samiksha-birthday-garden",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "15.1.4",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "framer-motion": "12.0.0-alpha.2",
    "gsap": "^3.12.5",
    "lucide-react": "^0.471.0"
  },
  "devDependencies": {
    "typescript": "^5.7.2",
    "@types/node": "^22.10.5",
    "@types/react": "^19.0.3",
    "@types/react-dom": "^19.0.2",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17"
  }
}"""

# ----------------------------------------------------
# 2. tsconfig.json
# ----------------------------------------------------
FILES_MAP["tsconfig.json"] = """{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}"""

# ----------------------------------------------------
# 3. next.config.ts
# ----------------------------------------------------
FILES_MAP["next.config.ts"] = """import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
};

export default nextConfig;"""

# ----------------------------------------------------
# 4. postcss.config.js
# ----------------------------------------------------
FILES_MAP["postcss.config.js"] = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};"""

# ----------------------------------------------------
# 5. tailwind.config.ts
# ----------------------------------------------------
FILES_MAP["tailwind.config.ts"] = """import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        garden: {
          bg: "#05050a",
          glowPrimary: "#ffd6e7",
          glowSecondary: "#ffb3d1",
          text: "#fff8fb",
          accent: "#f7c8da",
          darkMuted: "#1a1525",
        },
      },
      fontFamily: {
        serif: ["var(--font-serif)", "Georgia", "serif"],
        sans: ["var(--font-sans)", "Inter", "sans-serif"],
      },
      backgroundImage: {
        "vignette-radial": "radial-gradient(circle, transparent 40%, rgba(5,5,10,0.95) 100%)",
        "glow-radial": "radial-gradient(circle, var(--tw-gradient-stops))",
      },
    },
  },
  plugins: [],
};
export default config;"""

# ----------------------------------------------------
# 6. app/globals.css
# ----------------------------------------------------
FILES_MAP["app/globals.css"] = """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --font-serif: "Playfair Display", "Didot", "Georgia", serif;
  --font-sans: "Inter", system-ui, sans-serif;
  color-scheme: dark;
}

body {
  background-color: #05050a;
  color: #fff8fb;
  font-family: var(--font-sans);
  overflow-x: hidden;
  margin: 0;
  padding: 0;
}

.glass-panel {
  background: rgba(26, 21, 37, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 214, 231, 0.15);
}

.glass-button {
  background: rgba(255, 214, 231, 0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 214, 231, 0.2);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-button:hover {
  background: rgba(255, 214, 231, 0.18);
  border-color: rgba(255, 214, 231, 0.4);
  box-shadow: 0 0 15px rgba(255, 179, 209, 0.35);
}

.text-glow {
  text-shadow: 0 0 12px rgba(255, 214, 231, 0.6);
}

.text-glow-strong {
  text-shadow: 0 0 20px rgba(255, 179, 209, 0.9), 0 0 40px rgba(255, 214, 231, 0.4);
}

::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  background: #05050a;
}
::-webkit-scrollbar-thumb {
  background: rgba(255, 214, 231, 0.2);
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 214, 231, 0.45);
}

.sway-slow {
  transform-origin: bottom center;
}"""

# ----------------------------------------------------
# 7. app/layout.tsx
# ----------------------------------------------------
FILES_MAP["app/layout.tsx"] = """import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "A Moonlight Garden for Samiksha",
  description: "A magical interactive cinematic experience created with love for Samiksha's birthday.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..700&family=Inter:wght@300;400;500;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-garden-bg text-garden-text antialiased overflow-hidden select-none">
        {children}
      </body>
    </html>
  );
}"""

# ----------------------------------------------------
# 8. types/index.ts
# ----------------------------------------------------
FILES_MAP["types/index.ts"] = """export interface HeartItem {
  id: number;
  title: string;
  text: string;
}

export type BloomState = 
  | "ready" 
  | "blooming" 
  | "letter" 
  | "ending" 
  | "finished";

export interface Star {
  id: number;
  x: number;
  y: number;
  size: number;
  delay: number;
  duration: number;
}

export interface DustParticle {
  id: number;
  startX: number;
  startY: number;
  endX: number;
  endY: number;
  size: number;
  duration: number;
  delay: number;
}

export interface Petal {
  x: number;
  y: number;
  r: number;
  d: number;
  opacity: number;
  rotation: number;
  rotationSpeed: number;
  horizontalSpeed: number;
  verticalSpeed: number;
}"""

# ----------------------------------------------------
# 9. lib/synth.ts
# ----------------------------------------------------
FILES_MAP["lib/synth.ts"] = """"use client";

export class AmbientSynth {
  private ctx: AudioContext | null = null;
  private isPlaying: boolean = false;
  private activeNodes: AudioNode[] = [];
  private sequenceInterval: any = null;

  constructor() {}

  private init() {
    if (this.ctx) return;
    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
    if (AudioContextClass) {
      this.ctx = new AudioContextClass();
    }
  }

  public start() {
    this.init();
    if (!this.ctx || this.isPlaying) return;
    this.isPlaying = true;

    const masterGain = this.ctx.createGain();
    masterGain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    masterGain.connect(this.ctx.destination);
    this.activeNodes.push(masterGain);

    const chords = [
      [174.61, 220.00, 261.63, 329.63], 
      [261.63, 329.63, 392.00, 493.88], 
      [220.00, 261.63, 329.63, 440.00], 
      [196.00, 246.94, 293.66, 392.00], 
    ];

    let step = 0;
    const playNote = (freq: number, startTime: number, duration: number) => {
      if (!this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, startTime);

      gain.gain.setValueAtTime(0, startTime);
      gain.gain.linearRampToValueAtTime(0.12, startTime + 0.5);
      gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start(startTime);
      osc.stop(startTime + duration);
    };

    const playStep = () => {
      if (!this.ctx || !this.isPlaying) return;
      const now = this.ctx.currentTime;
      const chord = chords[step % chords.length];

      chord.forEach((freq, idx) => {
        playNote(freq, now + idx * 0.7, 5);
      });

      if (Math.random() > 0.4) {
        const highNote = chord[Math.floor(Math.random() * chord.length)] * 2;
        playNote(highNote, now + 3.0, 3);
      }

      step++;
    };

    playStep();
    this.sequenceInterval = setInterval(playStep, 6000);
  }

  public stop() {
    this.isPlaying = false;
    if (this.sequenceInterval) {
      clearInterval(this.sequenceInterval);
      this.sequenceInterval = null;
    }
    this.activeNodes.forEach((node) => {
      try {
        (node as any).disconnect();
      } catch (e) {}
    });
    this.activeNodes = [];
    if (this.ctx && this.ctx.state !== "closed") {
      this.ctx.close();
      this.ctx = null;
    }
  }
}"""

# ----------------------------------------------------
# 10. hooks/useReducedMotion.ts
# ----------------------------------------------------
FILES_MAP["hooks/useReducedMotion.ts"] = """"use client";

import { useEffect, useState } from "react";

export function useReducedMotion(): boolean {
  const [reduced, setReduced] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduced(mediaQuery.matches);

    const onChange = (event: MediaQueryListEvent) => {
      setReduced(event.matches);
    };

    mediaQuery.addEventListener("change", onChange);
    return () => mediaQuery.removeEventListener("change", onChange);
  }, []);

  return reduced;
}"""

# ----------------------------------------------------
# 11. hooks/useParallax.ts
# ----------------------------------------------------
FILES_MAP["hooks/useParallax.ts"] = """"use client";

import { useEffect, useState, useCallback } from "react";

export interface ParallaxOffset {
  x: number;
  y: number;
}

export function useParallax(strength: number = 20) {
  const [offset, setOffset] = useState<ParallaxOffset>({ x: 0, y: 0 });

  const handlePointerMove = useCallback(
    (e: PointerEvent) => {
      if (typeof window === "undefined") return;
      const { clientX, clientY } = e;
      const { innerWidth, innerHeight } = window;

      const relativeX = (clientX / innerWidth) - 0.5;
      const relativeY = (clientY / innerHeight) - 0.5;

      setOffset({
        x: relativeX * strength,
        y: relativeY * strength,
      });
    },
    [strength]
  );

  useEffect(() => {
    if (typeof window === "undefined") return;

    window.addEventListener("pointermove", handlePointerMove, { passive: true });
    return () => {
      window.removeEventListener("pointermove", handlePointerMove);
    };
  }, [handlePointerMove]);

  return offset;
}"""

# ----------------------------------------------------
# 12. hooks/useHeartProgress.ts
# ----------------------------------------------------
FILES_MAP["hooks/useHeartProgress.ts"] = """"use client";

import { useState, useCallback, useEffect } from "react";

const HEART_COUNT = 6;

export function useHeartProgress() {
  const [openedHearts, setOpenedHearts] = useState<number[]>([]);
  const [isUnlocked, setIsUnlocked] = useState(false);

  const openHeart = useCallback((id: number) => {
    setOpenedHearts((prev) => {
      if (prev.includes(id)) return prev;
      const updated = [...prev, id];
      return updated;
    });
  }, []);

  useEffect(() => {
    if (openedHearts.length === HEART_COUNT) {
      setIsUnlocked(true);
    }
  }, [openedHearts]);

  return {
    openedHearts,
    isUnlocked,
    openHeart,
    progressPercent: (openedHearts.length / HEART_COUNT) * 100,
    totalHearts: HEART_COUNT,
  };
}"""

# ----------------------------------------------------
# 13. hooks/useAudio.ts
# ----------------------------------------------------
FILES_MAP["hooks/useAudio.ts"] = """"use client";

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
}"""

# ----------------------------------------------------
# 14. hooks/useBloomSequence.ts
# ----------------------------------------------------
FILES_MAP["hooks/useBloomSequence.ts"] = """"use client";

import { useState, useCallback } from "react";

export type BloomState = 
  | "ready"       
  | "blooming"    
  | "letter"      
  | "ending"      
  | "finished";   

export function useBloomSequence() {
  const [bloomState, setBloomState] = useState<BloomState>("ready");

  const startBloom = useCallback(() => {
    setBloomState("blooming");
  }, []);

  const revealLetter = useCallback(() => {
    setBloomState("letter");
  }, []);

  const startEnding = useCallback(() => {
    setBloomState("ending");
  }, []);

  const resetAll = useCallback(() => {
    setBloomState("ready");
  }, []);

  return {
    bloomState,
    startBloom,
    revealLetter,
    startEnding,
    resetAll,
  };
}"""

# ----------------------------------------------------
# 15. components/StarField.tsx
# ----------------------------------------------------
FILES_MAP["components/StarField.tsx"] = """"use client";

import React, { useMemo } from "react";
import { motion } from "framer-motion";
import { useParallax } from "@/hooks/useParallax";

interface Star {
  id: number;
  x: number;
  y: number;
  size: number;
  delay: number;
  duration: number;
}

export function StarField() {
  const parallaxOffset = useParallax(15);

  const stars = useMemo(() => {
    const starList: Star[] = [];
    const seedRandom = (str: string) => {
      let hash = 0;
      for (let i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
      }
      return () => {
        const x = Math.sin(hash++) * 10000;
        return x - Math.floor(x);
      };
    };

    const rng = seedRandom("samiksha-birthday-night-garden");

    for (let i = 0; i < 140; i++) {
      starList.push({
        id: i,
        x: rng() * 100, 
        y: rng() * 100, 
        size: rng() * 1.8 + 0.8, 
        delay: rng() * 6,
        duration: rng() * 4 + 3,
      });
    }
    return starList;
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <motion.div
        className="relative w-full h-full"
        style={{
          x: parallaxOffset.x,
          y: parallaxOffset.y,
        }}
      >
        {stars.map((star) => (
          <motion.div
            key={star.id}
            className="absolute rounded-full bg-white"
            style={{
              left: `${star.x}%`,
              top: `${star.y}%`,
              width: star.size,
              height: star.size,
              boxShadow: star.size > 1.8 ? "0 0 6px #ffd6e7" : "none",
            }}
            animate={{
              opacity: [0.15, 0.95, 0.15],
              scale: [1, 1.25, 1],
            }}
            transition={{
              duration: star.duration,
              delay: star.delay,
              repeat: Infinity,
              ease: "easeInOut",
            }}
          />
        ))}
      </motion.div>
    </div>
  );
}"""

# ----------------------------------------------------
# 16. components/ParticleLayer.tsx
# ----------------------------------------------------
FILES_MAP["components/ParticleLayer.tsx"] = """"use client";

import React, { useMemo } from "react";
import { motion } from "framer-motion";
import { useParallax } from "@/hooks/useParallax";

interface DustParticle {
  id: number;
  startX: number;
  startY: number;
  endX: number;
  endY: number;
  size: number;
  duration: number;
  delay: number;
}

export function ParticleLayer() {
  const parallaxOffset = useParallax(35);

  const dustParticles = useMemo(() => {
    const list: DustParticle[] = [];
    const seedRandom = (str: string) => {
      let hash = 9831;
      for (let i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
      }
      return () => {
        const x = Math.sin(hash++) * 10000;
        return x - Math.floor(x);
      };
    };

    const rng = seedRandom("samiksha-crystal-garden-dust");

    for (let i = 0; i < 45; i++) {
      const startX = rng() * 100;
      const startY = rng() * 100;
      const endX = startX + (rng() * 14 - 7);
      const endY = startY - (rng() * 20 + 5);

      list.push({
        id: i,
        startX,
        startY,
        endX,
        endY,
        size: rng() * 3 + 2, 
        duration: rng() * 25 + 20, 
        delay: rng() * -20, 
      });
    }
    return list;
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <motion.div
        className="relative w-full h-full"
        style={{
          x: parallaxOffset.x * 1.5,
          y: parallaxOffset.y * 1.5,
        }}
      >
        {dustParticles.map((particle) => (
          <motion.div
            key={particle.id}
            className="absolute rounded-full"
            style={{
              background: "radial-gradient(circle, #ffd6e7 0%, rgba(255,179,209,0) 80%)",
              width: particle.size * 2,
              height: particle.size * 2,
              filter: "blur(0.5px)",
            }}
            initial={{
              x: `${particle.startX}%`,
              y: `${particle.startY}%`,
              opacity: 0,
            }}
            animate={{
              x: [`${particle.startX}%`, `${particle.endX}%`],
              y: [`${particle.startY}%`, `${particle.endY}%`],
              opacity: [0, 0.45, 0.75, 0.45, 0],
            }}
            transition={{
              duration: particle.duration,
              delay: particle.delay,
              repeat: Infinity,
              ease: "linear",
            }}
          />
        ))}
      </motion.div>
    </div>
  );
}"""

# ----------------------------------------------------
# 17. components/BackgroundScene.tsx
# ----------------------------------------------------
FILES_MAP["components/BackgroundScene.tsx"] = """"use client";

import React from "react";
import { StarField } from "./StarField";
import { ParticleLayer } from "./ParticleLayer";

export function BackgroundScene() {
  return (
    <div className="absolute inset-0 w-full h-full bg-[#05050a] overflow-hidden -z-10 select-none">
      <div 
        className="absolute w-[60vw] h-[60vw] rounded-full blur-[140px] opacity-25 pointer-events-none"
        style={{
          top: "15%",
          left: "20%",
          background: "radial-gradient(circle, #ffb3d1 0%, rgba(255,179,209,0) 70%)"
        }}
      />
      
      <div 
        className="absolute w-[70vw] h-[70vw] rounded-full blur-[160px] opacity-20 pointer-events-none"
        style={{
          bottom: "10%",
          right: "15%",
          background: "radial-gradient(circle, #ffd6e7 0%, rgba(255,214,231,0) 75%)"
        }}
      />

      <div 
        className="absolute w-[50vw] h-[50vw] rounded-full blur-[130px] opacity-[0.12] pointer-events-none"
        style={{
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          background: "radial-gradient(circle, #f7c8da 0%, rgba(247,200,218,0) 70%)"
        }}
      />

      <StarField />
      <ParticleLayer />

      <div className="absolute inset-0 bg-vignette-radial pointer-events-none" />
    </div>
  );
}"""

# ----------------------------------------------------
# 18. components/AudioManager.tsx
# ----------------------------------------------------
FILES_MAP["components/AudioManager.tsx"] = """"use client";

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
}"""

# ----------------------------------------------------
# 19. components/CrystalTulip.tsx
# ----------------------------------------------------
FILES_MAP["components/CrystalTulip.tsx"] = """"use client";

import React, { useRef } from "react";
import { motion } from "framer-motion";

interface CrystalTulipProps {
  isUnlocked: boolean;
  bloomProgress: number; 
  onClick: () => void;
  state: "ready" | "blooming" | "letter" | "ending" | "finished";
}

export function CrystalTulip({ isUnlocked, bloomProgress, onClick, state }: CrystalTulipProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  const canBeClicked = isUnlocked && state === "ready";

  return (
    <div
      ref={containerRef}
      className="relative flex flex-col items-center justify-center cursor-pointer select-none"
      onClick={() => {
        if (canBeClicked) {
          onClick();
        }
      }}
    >
      {canBeClicked && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: [0.4, 0.9, 0.4], y: 0 }}
          transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
          className="absolute -top-16 text-xs uppercase tracking-[0.2em] text-garden-glowPrimary text-center pointer-events-none text-shadow font-serif"
        >
          Touch the glass flower to bloom
        </motion.div>
      )}

      <motion.div
        className="absolute w-56 h-56 rounded-full -z-10 pointer-events-none"
        style={{
          background: "radial-gradient(circle, rgba(255,179,209,0.3) 0%, rgba(255,214,231,0) 70%)",
        }}
        animate={{
          scale: canBeClicked ? [1, 1.15, 1] : [1, 1.05, 1],
          opacity: canBeClicked ? [0.6, 0.9, 0.6] : [0.4, 0.6, 0.4],
        }}
        transition={{
          duration: 4,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      <motion.div
        className="sway-slow"
        animate={{
          rotate: [0, -1.5, 0, 1.5, 0],
          y: [0, -4, 0, 4, 0],
        }}
        transition={{
          duration: 6,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        style={{
          transformOrigin: "bottom center",
        }}
      >
        <svg
          width="260"
          height="340"
          viewBox="0 0 200 300"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="filter drop-shadow-[0_0_15px_rgba(255,214,231,0.35)]"
        >
          <defs>
            <linearGradient id="stemGrad" x1="100" y1="290" x2="100" y2="150" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#0d2818" />
              <stop offset="50%" stopColor="#1e4d2b" />
              <stop offset="100%" stopColor="#43aa8b" />
            </linearGradient>

            <linearGradient id="leafGradLeft" x1="50" y1="240" x2="100" y2="200" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#132a13" stopOpacity="0.7" />
              <stop offset="100%" stopColor="#4f772d" stopOpacity="0.9" />
            </linearGradient>

            <linearGradient id="leafGradRight" x1="150" y1="230" x2="100" y2="190" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#132a13" stopOpacity="0.7" />
              <stop offset="100%" stopColor="#4f772d" stopOpacity="0.9" />
            </linearGradient>

            <linearGradient id="petalGlowGrad" x1="100" y1="180" x2="100" y2="70" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#ffb3d1" stopOpacity="0.85" />
              <stop offset="60%" stopColor="#ffd6e7" stopOpacity="0.95" />
              <stop offset="100%" stopColor="#ffffff" stopOpacity="1" />
            </linearGradient>

            <linearGradient id="outerPetalGrad" x1="60" y1="180" x2="140" y2="90" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#ff70a6" stopOpacity="0.4" />
              <stop offset="50%" stopColor="#ffb3d1" stopOpacity="0.7" />
              <stop offset="100%" stopColor="#ffd6e7" stopOpacity="0.9" />
            </linearGradient>

            <linearGradient id="shineGrad" x1="100" y1="60" x2="110" y2="200" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#ffffff" stopOpacity="0.8" />
              <stop offset="30%" stopColor="#ffffff" stopOpacity="0.1" />
              <stop offset="100%" stopColor="#ffd6e7" stopOpacity="0" />
            </linearGradient>
          </defs>

          <path
            d="M100,160 Q101,225 100,290"
            stroke="url(#stemGrad)"
            strokeWidth="5"
            strokeLinecap="round"
          />

          <path
            d="M100,250 Q60,230 45,185 Q75,195 100,220 Z"
            fill="url(#leafGradLeft)"
            stroke="#43aa8b"
            strokeWidth="1"
            opacity="0.85"
          />

          <path
            d="M100,235 Q140,215 155,170 Q125,180 100,205 Z"
            fill="url(#leafGradRight)"
            stroke="#43aa8b"
            strokeWidth="1"
            opacity="0.85"
          />

          <path
            d="M90,165 Q100,172 110,165 Q105,152 95,152 Z"
            fill="#1e4d2b"
            opacity="0.9"
          />

          <circle
            cx="100"
            cy="125"
            r="24"
            fill="url(#petalGlowGrad)"
            filter="blur(8px)"
            opacity={canBeClicked ? 0.8 : 0.45 + bloomProgress * 0.55}
          />

          <path
            d="M100,65 Q85,110 82,145 Q100,160 118,145 Q115,110 100,65 Z"
            fill="url(#petalGlowGrad)"
            stroke="#ffd6e7"
            strokeWidth="1.5"
            opacity="0.95"
            transform={`translate(0, ${-25 * bloomProgress}) scale(${1 + 0.15 * bloomProgress})`}
            style={{ transformOrigin: "100px 150px" }}
          />

          <path
            d="M100,75 Q75,100 70,140 Q90,152 100,140 Z"
            fill="url(#outerPetalGrad)"
            stroke="#ffb3d1"
            strokeWidth="1"
            opacity="0.8"
            transform={`rotate(${-35 * bloomProgress}, 100, 150)`}
            style={{ transformOrigin: "100px 150px" }}
          />

          <path
            d="M100,75 Q125,100 130,140 Q110,152 100,140 Z"
            fill="url(#outerPetalGrad)"
            stroke="#ffb3d1"
            strokeWidth="1"
            opacity="0.8"
            transform={`rotate(${35 * bloomProgress}, 100, 150)`}
            style={{ transformOrigin: "100px 150px" }}
          />

          <path
            d="M95,85 Q55,105 60,155 Q85,168 100,150 Z"
            fill="url(#outerPetalGrad)"
            stroke="#f7c8da"
            strokeWidth="1"
            opacity="0.85"
            transform={`rotate(${-48 * bloomProgress}, 100, 160)`}
            style={{ transformOrigin: "100px 160px" }}
          />

          <path
            d="M105,85 Q145,105 140,155 Q115,168 100,150 Z"
            fill="url(#outerPetalGrad)"
            stroke="#f7c8da"
            strokeWidth="1"
            opacity="0.85"
            transform={`rotate(${48 * bloomProgress}, 100, 160)`}
            style={{ transformOrigin: "100px 160px" }}
          />

          <path
            d="M100,70 Q88,110 88,140"
            stroke="url(#shineGrad)"
            strokeWidth="2.5"
            strokeLinecap="round"
            opacity="0.75"
          />
          <path
            d="M93,95 Q70,115 72,145"
            stroke="url(#shineGrad)"
            strokeWidth="1.5"
            strokeLinecap="round"
            opacity="0.6"
          />
        </svg>
      </motion.div>
    </div>
  );
}"""

# ----------------------------------------------------
# 20. components/HeartNode.tsx
# ----------------------------------------------------
FILES_MAP["components/HeartNode.tsx"] = """"use client";

import React from "react";
import { motion } from "framer-motion";
import { Sparkles, Heart } from "lucide-react";

interface HeartNodeProps {
  id: number;
  title: string;
  angle: number; 
  radius: number; 
  isOpened: boolean;
  onClick: () => void;
}

export function HeartNode({ id, title, angle, radius, isOpened, onClick }: HeartNodeProps) {
  const rad = (angle * Math.PI) / 180;
  const x = Math.cos(rad) * radius;
  const y = Math.sin(rad) * radius;

  return (
    <motion.div
      className="absolute z-20 cursor-pointer"
      style={{
        left: "50%",
        top: "50%",
      }}
      animate={{
        x: [x - 4, x + 4, x - 4],
        y: [y - 4, y + 4, y - 4],
      }}
      transition={{
        duration: 4 + (id % 3),
        repeat: Infinity,
        ease: "easeInOut",
      }}
      whileHover={{ scale: 1.12, zIndex: 30 }}
      whileTap={{ scale: 0.95 }}
      onClick={(e) => {
        e.stopPropagation();
        onClick();
      }}
    >
      <div className="relative -left-1/2 -top-1/2 flex flex-col items-center">
        <div
          className={`w-14 h-14 rounded-full flex items-center justify-center transition-all duration-500 relative ${
            isOpened
              ? "glass-button border-garden-glowPrimary shadow-[0_0_20px_rgba(255,214,231,0.5)] text-garden-glowPrimary"
              : "glass-panel text-garden-accent hover:border-garden-glowSecondary hover:text-garden-glowSecondary"
          }`}
        >
          {isOpened ? (
            <Sparkles className="w-5 h-5 animate-pulse" />
          ) : (
            <Heart className="w-5 h-5 fill-current opacity-70" />
          )}

          <span className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-garden-glowPrimary shadow-[0_0_8px_#ffd6e7]" />
        </div>

        <span className="mt-2 text-[10px] tracking-[0.18em] uppercase text-garden-text/70 whitespace-nowrap bg-garden-bg/80 px-2 py-0.5 rounded border border-white/5 font-serif">
          {title}
        </span>
      </div>
    </motion.div>
  );
}"""

# ----------------------------------------------------
# 21. components/HeartModal.tsx
# ----------------------------------------------------
FILES_MAP["components/HeartModal.tsx"] = """"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, Sparkles } from "lucide-react";

interface HeartModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  text: string;
}

export function HeartModal({ isOpen, onClose, title, text }: HeartModalProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="absolute inset-0 bg-black/60 backdrop-blur-md"
          />

          <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 20 }}
            transition={{ type: "spring", duration: 0.6 }}
            className="relative w-full max-w-md glass-panel p-8 rounded-2xl shadow-2xl border border-garden-glowPrimary/25 overflow-hidden z-10"
          >
            <div className="absolute -top-12 -left-12 w-32 h-32 rounded-full bg-garden-glowSecondary/15 blur-2xl pointer-events-none" />

            <button
              onClick={onClose}
              className="absolute top-4 right-4 p-2 text-garden-accent hover:text-white rounded-full bg-white/5 hover:bg-white/10 transition-colors focus:outline-none focus:ring-1 focus:ring-garden-glowPrimary"
              aria-label="Close modal"
            >
              <X className="w-4 h-4" />
            </button>

            <div className="flex items-center gap-2 mb-4 text-garden-glowPrimary">
              <Sparkles className="w-5 h-5" />
              <span className="text-[10px] tracking-[0.25em] uppercase font-sans font-medium">
                Samiksha's Dream Garden
              </span>
            </div>

            <h3 className="text-2xl font-serif text-white font-semibold mb-4 leading-tight tracking-wide">
              {title}
            </h3>

            <div className="h-[1px] w-12 bg-gradient-to-r from-garden-glowSecondary to-transparent mb-5" />

            <p className="text-garden-accent/90 leading-relaxed font-sans text-sm italic sm:text-base">
              "{text}"
            </p>

            <div className="mt-8 flex justify-end">
              <button
                onClick={onClose}
                className="glass-button px-5 py-2 text-xs uppercase tracking-widest text-garden-glowPrimary rounded-lg focus:outline-none focus:ring-1 focus:ring-garden-glowPrimary"
              >
                Close thoughts
              </button>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}"""

# ----------------------------------------------------
# 22. components/HeartOrbit.tsx
# ----------------------------------------------------
FILES_MAP["components/HeartOrbit.tsx"] = """"use client";

import React, { useState, useEffect } from "react";
import { HeartNode } from "./HeartNode";

interface HeartItem {
  id: number;
  title: string;
  text: string;
}

interface HeartOrbitProps {
  hearts: HeartItem[];
  openedHearts: number[];
  onOpenNode: (id: number, title: string, text: string) => void;
}

export function HeartOrbit({ hearts, openedHearts, onOpenNode }: HeartOrbitProps) {
  const [radius, setRadius] = useState(135);

  useEffect(() => {
    if (typeof window === "undefined") return;

    const handleResize = () => {
      if (window.innerWidth < 640) {
        setRadius(110); 
      } else if (window.innerWidth < 1024) {
        setRadius(135);
      } else {
        setRadius(165); 
      }
    };

    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none z-10 flex items-center justify-center">
      <div
        className="absolute rounded-full border border-dashed border-garden-glowPrimary/10 pointer-events-none transition-all duration-300"
        style={{
          width: radius * 2,
          height: radius * 2,
        }}
      />

      {hearts.map((heart, index) => {
        const angle = (360 / hearts.length) * index - 90; 
        const isOpened = openedHearts.includes(heart.id);

        return (
          <HeartNode
            key={heart.id}
            id={heart.id}
            title={heart.title}
            angle={angle}
            radius={radius}
            isOpened={isOpened}
            onClick={() => onOpenNode(heart.id, heart.title, heart.text)}
          />
        );
      })}
    </div>
  );
}"""

# ----------------------------------------------------
# 23. components/ProgressTracker.tsx
# ----------------------------------------------------
FILES_MAP["components/ProgressTracker.tsx"] = """"use client";

import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Lock, Unlock } from "lucide-react";

interface ProgressTrackerProps {
  openedCount: number;
  totalCount: number;
  isUnlocked: boolean;
}

export function ProgressTracker({ openedCount, totalCount, isUnlocked }: ProgressTrackerProps) {
  const percentage = (openedCount / totalCount) * 100;

  return (
    <div className="w-full max-w-sm glass-panel px-6 py-4 rounded-xl flex flex-col items-center gap-2.5 shadow-lg border border-white/5 relative z-30 select-none">
      <div className="w-full flex justify-between items-center text-xs tracking-wider uppercase text-garden-accent/90">
        <span className="font-serif">Secret thoughts unlocked</span>
        <span className="font-sans font-medium">
          {openedCount} / {totalCount}
        </span>
      </div>

      <div className="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
        <motion.div
          className="h-full bg-gradient-to-r from-garden-glowSecondary to-garden-glowPrimary"
          initial={{ width: 0 }}
          animate={{ width: `${percentage}%` }}
          transition={{ duration: 0.5, ease: "easeOut" }}
          style={{
            boxShadow: "0 0 10px rgba(255,214,231,0.6)",
          }}
        />
      </div>

      <div className="w-full mt-1.5 flex items-center justify-center">
        <AnimatePresence mode="wait">
          {isUnlocked ? (
            <motion.div
              key="unlocked"
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -5 }}
              className="flex items-center gap-1.5 text-xs text-garden-glowPrimary tracking-wide font-sans font-medium"
            >
              <Unlock className="w-3.5 h-3.5" />
              <span>Something beautiful is waiting inside the flower...</span>
            </motion.div>
          ) : (
            <motion.div
              key="locked"
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -5 }}
              className="flex items-center gap-1.5 text-xs text-garden-accent/60 tracking-wide font-sans"
            >
              <Lock className="w-3.5 h-3.5 opacity-60" />
              <span>Reveal all 6 stars to unlock the tulip</span>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}"""

# ----------------------------------------------------
# 24. components/BloomController.tsx
# ----------------------------------------------------
FILES_MAP["components/BloomController.tsx"] = """"use client";

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

  useEffect(() => {
    if (!isActive) return;

    const tl = gsap.timeline({
      onComplete: () => {
        onComplete();
      },
    });

    const bloomObj = { progress: 0 };

    tl.to(overlayRef.current, {
      opacity: 0.95,
      duration: 1.5,
      ease: "power2.out",
      onStart: () => setStageText("The garden fades as the stars align..."),
    });

    tl.to(overlayRef.current, {
      backgroundColor: "#11071c",
      duration: 1.2,
      ease: "power1.inOut",
      onStart: () => setStageText("A quiet energy gathers at the stem..."),
    });

    tl.to(bloomObj, {
      progress: 1,
      duration: 3.2,
      ease: "power2.inOut",
      onUpdate: () => {
        onTimelineProgress(bloomObj.progress);
        if (bloomObj.progress > 0.25 && bloomObj.progress < 0.7) {
          setStageText("The translucent glass petals slowly unfold...");
        } else if (bloomObj.progress >= 0.7) {
          setStageText("The core begins to crystallize into light...");
        }
      },
    });

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

    tl.to({}, { duration: 0.8 });

    return () => {
      tl.kill();
    };
  }, [isActive, onTimelineProgress, onComplete]);

  if (!isActive) return null;

  return (
    <div className="fixed inset-0 z-40 pointer-events-none overflow-hidden flex flex-col items-center justify-center">
      <div
        ref={overlayRef}
        className="absolute inset-0 bg-[#020206] opacity-0 transition-all duration-300 pointer-events-auto"
      />

      <div
        ref={flashRef}
        className="absolute inset-0 bg-gradient-to-tr from-[#fff0f5] via-[#ffd6e7] to-white opacity-0 mix-blend-overlay pointer-events-none"
      />

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
}"""

# ----------------------------------------------------
# 25. components/LetterReveal.tsx
# ----------------------------------------------------
FILES_MAP["components/LetterReveal.tsx"] = """"use client";

import React, { useRef, useEffect } from "react";
import { motion } from "framer-motion";
import { Heart, Sparkles } from "lucide-react";
import gsap from "gsap";

interface LetterRevealProps {
  onClose: () => void;
}

export function LetterReveal({ onClose }: LetterRevealProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const textContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!textContainerRef.current) return;
    const paragraphs = textContainerRef.current.querySelectorAll(".reveal-p");

    gsap.fromTo(
      paragraphs,
      {
        opacity: 0,
        y: 24,
      },
      {
        opacity: 1,
        y: 0,
        stagger: 0.22,
        duration: 1.4,
        ease: "power3.out",
        delay: 0.5,
      }
    );
  }, []);

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto px-4 py-12 flex items-center justify-center bg-black/40 backdrop-blur-xl">
      <motion.div
        ref={containerRef}
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.95 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="relative w-full max-w-2xl glass-panel p-8 md:p-12 rounded-3xl shadow-2xl border border-garden-glowPrimary/30 overflow-hidden my-auto"
      >
        <div className="absolute -top-32 -right-32 w-80 h-80 rounded-full bg-garden-glowPrimary/10 blur-[80px] pointer-events-none" />
        <div className="absolute -bottom-32 -left-32 w-80 h-80 rounded-full bg-garden-glowSecondary/10 blur-[80px] pointer-events-none" />

        <div className="flex flex-col items-center gap-1.5 mb-8 text-center">
          <Sparkles className="w-6 h-6 text-garden-glowPrimary animate-pulse" />
          <span className="text-[10px] tracking-[0.3em] uppercase text-garden-glowSecondary font-sans">
            A Letter of Light
          </span>
        </div>

        <div
          ref={textContainerRef}
          className="max-h-[60vh] overflow-y-auto pr-4 text-garden-text space-y-6 md:space-y-7 text-sm md:text-base leading-relaxed font-serif tracking-wide select-text"
        >
          <h2 className="reveal-p text-xl md:text-2xl font-semibold text-white tracking-wide border-b border-white/10 pb-4">
            For Samiksha,
          </h2>

          <p className="reveal-p text-garden-accent">
            There are flowers that bloom for a season,
          </p>

          <p className="reveal-p text-garden-accent">
            and there are souls that make every season feel like spring.
          </p>

          <p className="reveal-p font-medium text-white">
            You have always been one of those rare souls.
          </p>

          <p className="reveal-p text-garden-text/90">
            The kind that brings warmth without trying, <br />
            comfort without speaking, <br />
            and joy without asking for anything in return.
          </p>

          <p className="reveal-p text-garden-text/90">
            The world can often move too fast, <br />
            yet somehow you carry a gentleness that reminds people <br />
            to slow down and appreciate what truly matters.
          </p>

          <p className="reveal-p text-garden-glowPrimary font-medium italic text-center py-4 bg-white/5 rounded-xl border border-white/5">
            You have a beautiful way of existing.
          </p>

          <div className="reveal-p space-y-2 text-center text-garden-text/80">
            <p className="italic">Not loudly.</p>
            <p className="italic">Not dramatically.</p>
            <p className="italic">But in a way that leaves every place brighter than before.</p>
          </div>

          <p className="reveal-p text-garden-text/90">
            If kindness had a face, <br />
            if grace had a voice, <br />
            if sunshine could walk beside someone,
          </p>

          <p className="reveal-p text-white font-medium">
            I imagine it would look a little like you.
          </p>

          <p className="reveal-p text-garden-accent">
            Today is your birthday, <br />
            but this little garden of stars and tulips exists for a different reason:
          </p>

          <p className="reveal-p text-garden-glowPrimary text-shadow">
            to remind you how beautiful you are, <br />
            not just today, <br />
            but on every ordinary day in between.
          </p>

          <p className="reveal-p text-xl font-medium pt-4 text-white">
            Happy Birthday, Samiksha.
          </p>

          <div className="reveal-p pt-4 border-t border-white/10 flex flex-col items-end">
            <span className="text-xs uppercase tracking-widest text-garden-glowSecondary">
              With love,
            </span>
            <span className="text-lg font-semibold text-white mt-1">Raj</span>
          </div>
        </div>

        <div className="mt-10 flex justify-center">
          <button
            onClick={onClose}
            className="glass-button px-8 py-3 rounded-xl flex items-center gap-2 text-sm uppercase tracking-widest text-garden-glowPrimary font-sans transition-all focus:outline-none focus:ring-1 focus:ring-garden-glowPrimary"
          >
            <Heart className="w-4 h-4 fill-current" />
            <span>Close Letter</span>
          </button>
        </div>
      </motion.div>
    </div>
  );
}"""

# ----------------------------------------------------
# 26. components/PetalRain.tsx
# ----------------------------------------------------
FILES_MAP["components/PetalRain.tsx"] = """"use client";

import React, { useEffect, useRef } from "react";

interface Petal {
  x: number;
  y: number;
  r: number;
  d: number;
  opacity: number;
  rotation: number;
  rotationSpeed: number;
  horizontalSpeed: number;
  verticalSpeed: number;
}

export function PetalRain() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrameId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };
    window.addEventListener("resize", handleResize);

    const petals: Petal[] = [];
    const maxPetals = 85;

    for (let i = 0; i < maxPetals; i++) {
      petals.push({
        x: Math.random() * width,
        y: Math.random() * height - height,
        r: Math.random() * 8 + 6, 
        d: Math.random() + 0.5,
        opacity: Math.random() * 0.6 + 0.35,
        rotation: Math.random() * 360,
        rotationSpeed: Math.random() * 1.5 - 0.75,
        horizontalSpeed: Math.random() * 1.5 - 0.75,
        verticalSpeed: Math.random() * 1.5 + 1.0,
      });
    }

    const drawPetal = (
      ctx: CanvasRenderingContext2D,
      x: number,
      y: number,
      r: number,
      rotation: number,
      opacity: number
    ) => {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate((rotation * Math.PI) / 180);
      ctx.beginPath();
      
      ctx.moveTo(0, 0);
      ctx.quadraticCurveTo(-r / 1.5, -r / 1.5, -r, 0);
      ctx.quadraticCurveTo(-r / 1.5, r / 1.5, 0, r);
      ctx.quadraticCurveTo(r / 1.5, r / 1.5, r, 0);
      ctx.quadraticCurveTo(r / 1.5, -r / 1.5, 0, 0);

      const gradient = ctx.createLinearGradient(-r, -r, r, r);
      gradient.addColorStop(0, `rgba(255, 214, 231, ${opacity})`);
      gradient.addColorStop(0.5, `rgba(255, 179, 210, ${opacity * 0.85})`);
      gradient.addColorStop(1, `rgba(247, 200, 218, ${opacity * 0.5})`);

      ctx.fillStyle = gradient;
      ctx.fill();

      ctx.strokeStyle = `rgba(255, 255, 255, ${opacity * 0.3})`;
      ctx.lineWidth = 0.5;
      ctx.stroke();

      ctx.restore();
    };

    const update = () => {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < maxPetals; i++) {
        const petal = petals[i];
        petal.y += petal.verticalSpeed;
        petal.x += petal.horizontalSpeed + Math.sin(petal.y / 30) * 0.5;
        petal.rotation += petal.rotationSpeed;

        if (petal.y > height + 20) {
          petal.y = -20;
          petal.x = Math.random() * width;
          petal.verticalSpeed = Math.random() * 1.5 + 1.0;
          petal.horizontalSpeed = Math.random() * 1.5 - 0.75;
        }

        if (petal.x > width + 20) {
          petal.x = -20;
        } else if (petal.x < -20) {
          petal.x = width + 20;
        }

        drawPetal(ctx, petal.x, petal.y, petal.r, petal.rotation, petal.opacity);
      }

      animationFrameId = requestAnimationFrame(update);
    };

    update();

    return () => {
      window.removeEventListener("resize", handleResize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return <canvas ref={canvasRef} className="fixed inset-0 pointer-events-none z-30" />;
}"""

# ----------------------------------------------------
# 27. components/EndingSequence.tsx
# ----------------------------------------------------
FILES_MAP["components/EndingSequence.tsx"] = """"use client";

import React, { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export function EndingSequence() {
  const [step, setStep] = useState(0);

  useEffect(() => {
    const timer1 = setTimeout(() => {
      setStep(1); 
    }, 1500);

    const timer2 = setTimeout(() => {
      setStep(2); 
    }, 6000);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
    };
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-[#030308]/95 px-6 text-center select-none">
      <div className="absolute w-[80vw] h-[80vw] max-w-4xl rounded-full bg-garden-glowSecondary/10 blur-[130px] pointer-events-none" />

      <AnimatePresence mode="wait">
        {step === 1 && (
          <motion.div
            key="poem"
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -15 }}
            transition={{ duration: 1.8, ease: "easeInOut" }}
            className="space-y-4 max-w-xl"
          >
            <p className="text-xl sm:text-2xl font-serif italic text-garden-glowPrimary/90 leading-relaxed text-glow">
              "Some flowers bloom in gardens."
            </p>
            <p className="text-2xl sm:text-3xl font-serif italic text-white leading-relaxed text-glow-strong">
              "Mine grew up beside me."
            </p>
          </motion.div>
        )}

        {step === 2 && (
          <motion.div
            key="greetings"
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 2.2, ease: "easeOut" }}
            className="flex flex-col items-center space-y-6"
          >
            <div className="relative">
              <span className="absolute -top-6 -left-6 w-3 h-3 rounded-full bg-garden-glowPrimary/60 blur-[2px] animate-ping" />
              <h1 className="text-4xl sm:text-6xl font-serif font-bold text-white tracking-wide text-glow-strong leading-tight">
                Happy Birthday, <br />
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-garden-glowPrimary via-garden-accent to-garden-glowSecondary">
                  Samiksha
                </span>
              </h1>
            </div>

            <p className="text-xs sm:text-sm tracking-[0.25em] uppercase text-garden-accent/75 font-sans pt-4 max-w-md">
              Wishing you a beautiful journey through the stars and may all your magical wishes bloom.
            </p>

            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 0.6 }}
              transition={{ delay: 2.5, duration: 1 }}
              className="pt-10 text-[10px] tracking-widest text-garden-accent/40 font-serif"
            >
              designed with endless love &bull; Raj
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}"""

# ----------------------------------------------------
# 28. app/page.tsx
# ----------------------------------------------------
FILES_MAP["app/page.tsx"] = """"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { BackgroundScene } from "@/components/BackgroundScene";
import { AudioManager } from "@/components/AudioManager";
import { CrystalTulip } from "@/components/CrystalTulip";
import { HeartOrbit } from "@/components/HeartOrbit";
import { HeartModal } from "@/components/HeartModal";
import { ProgressTracker } from "@/components/ProgressTracker";
import { BloomController } from "@/components/BloomController";
import { LetterReveal } from "@/components/LetterReveal";
import { PetalRain } from "@/components/PetalRain";
import { EndingSequence } from "@/components/EndingSequence";

import { useAudio } from "@/hooks/useAudio";
import { useHeartProgress } from "@/hooks/useHeartProgress";
import { useBloomSequence } from "@/hooks/useBloomSequence";

const HEARTS_DATA = [
  {
    id: 1,
    title: "A Little Thought",
    text: "Some people leave footprints. You leave flowers wherever you go.",
  },
  {
    id: 2,
    title: "A Little Wonder",
    text: "There are people who brighten a room. You brighten entire days.",
  },
  {
    id: 3,
    title: "A Little Magic",
    text: "Kindness is invisible until someone like you makes it impossible to ignore.",
  },
  {
    id: 4,
    title: "A Little Star",
    text: "The stars decorate the sky. Your smile decorates every memory.",
  },
  {
    id: 5,
    title: "A Little Secret",
    text: "You carry a quiet kind of magic—the kind that makes people feel at home.",
  },
  {
    id: 6,
    title: "A Little Bloom",
    text: "The world keeps changing, but your heart has always remained beautiful.",
  },
];

export default function Home() {
  const audioState = useAudio();
  const { openedHearts, isUnlocked, openHeart } = useHeartProgress();
  const { bloomState, startBloom, revealLetter, startEnding } = useBloomSequence();

  const [activeModal, setActiveModal] = useState<{
    isOpen: boolean;
    title: string;
    text: string;
  }>({
    isOpen: false,
    title: "",
    text: "",
  });

  const [bloomProgress, setBloomProgress] = useState(0);
  const [hasInteracted, setHasInteracted] = useState(false);

  const handleOpenNode = (id: number, title: string, text: string) => {
    setActiveModal({ isOpen: true, title, text });
    openHeart(id);
  };

  const handleCloseModal = () => {
    setActiveModal((prev) => ({ ...prev, isOpen: false }));
  };

  const handleExploreEnter = () => {
    setHasInteracted(true);
    audioState.play();
  };

  return (
    <main className="relative w-screen h-screen overflow-hidden flex flex-col items-center justify-between p-6 sm:p-8">
      <BackgroundScene />

      <AnimatePresence>
        {!hasInteracted && (
          <motion.div
            key="intro-screen"
            initial={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1 }}
            className="fixed inset-0 z-[100] flex flex-col items-center justify-center bg-[#05050a] p-6 text-center"
          >
            <div className="absolute w-[60vw] h-[60vw] bg-garden-glowPrimary/15 rounded-full blur-[120px] pointer-events-none" />

            <motion.div
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ delay: 0.2, duration: 1, ease: "easeOut" }}
              className="max-w-md space-y-6 relative z-10"
            >
              <h2 className="text-sm tracking-[0.3em] uppercase text-garden-glowSecondary font-sans font-semibold">
                Welcome to
              </h2>
              <h1 className="text-3xl sm:text-4xl font-serif text-white tracking-wide font-medium leading-tight">
                Samiksha's <br />
                Moonlit Garden
              </h1>
              <p className="text-xs sm:text-sm text-garden-accent/80 leading-relaxed font-serif italic max-w-xs mx-auto">
                "Some secrets bloom only under the quiet watch of the stars."
              </p>

              <button
                onClick={handleExploreEnter}
                className="glass-button px-8 py-3 rounded-xl text-xs uppercase tracking-[0.2em] text-garden-glowPrimary font-sans transition-all duration-300 focus:outline-none focus:ring-1 focus:ring-garden-glowPrimary mt-6"
              >
                Enter the Garden
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {hasInteracted && bloomState === "ready" && (
        <>
          <motion.header
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="w-full flex flex-col items-center text-center mt-4 pointer-events-none z-10"
          >
            <h1 className="text-2xl sm:text-3xl font-serif text-white tracking-wide font-medium leading-normal text-glow">
              Samiksha's Garden
            </h1>
            <p className="text-[10px] tracking-[0.22em] uppercase text-garden-accent/70 mt-1">
              Reveal the secret stars to find her flower
            </p>
          </motion.header>

          <div className="relative w-full h-[55vh] flex items-center justify-center">
            <div className="relative z-10">
              <CrystalTulip
                isUnlocked={isUnlocked}
                bloomProgress={bloomProgress}
                onClick={startBloom}
                state={bloomState}
              />
            </div>

            <HeartOrbit
              hearts={HEARTS_DATA}
              openedHearts={openedHearts}
              onOpenNode={handleOpenNode}
            />
          </div>

          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="mb-6 z-20"
          >
            <ProgressTracker
              openedCount={openedHearts.length}
              totalCount={HEARTS_DATA.length}
              isUnlocked={isUnlocked}
            />
          </motion.div>
        </>
      )}

      <HeartModal
        isOpen={activeModal.isOpen}
        onClose={handleCloseModal}
        title={activeModal.title}
        text={activeModal.text}
      />

      <BloomController
        isActive={bloomState === "blooming"}
        onTimelineProgress={(val) => setBloomProgress(val)}
        onComplete={revealLetter}
      />

      <AnimatePresence>
        {bloomState === "letter" && (
          <LetterReveal
            onClose={() => {
              startEnding();
            }}
          />
        )}
      </AnimatePresence>

      {hasInteracted && <AudioManager audioState={audioState} />}

      {(bloomState === "ending" || bloomState === "finished" || bloomState === "letter") && (
        <PetalRain />
      )}

      {bloomState === "ending" && <EndingSequence />}
    </main>
  );
}"""

# ----------------------------------------------------
# Project Generator & Zip Execution Driver
# ----------------------------------------------------
def main():
    print("[*] Launching automatic project folder generation script...")
    root = Path(".")
    
    # Write every file automatically
    for filepath_str, code_content in FILES_MAP.items():
        destination = root / filepath_str
        destination.parent.mkdir(parents=True, exist_ok=True)
        print(f" -> Creating: {filepath_str}")
        destination.write_text(code_content.strip(), encoding="utf-8")

    # Generate public/audio structure
    audio_dir = root / "public" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    (audio_dir / "placeholder.txt").write_text(
        "Place your optional piano.mp3 audio file inside this directory for background soundtrack playback.",
        encoding="utf-8"
    )

    # Compress the output files automatically into samiksha-birthday.zip
    zip_filename = "samiksha-birthday.zip"
    print(f"[*] Packaging project files into: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for filepath_str in FILES_MAP.keys():
            zf.write(filepath_str)
        zf.write("public/audio/placeholder.txt")

    print("[+] Done! All files generated successfully on disk. Run 'python3 generate_project.py' and enjoy.")

if __name__ == "__main__":
    main()