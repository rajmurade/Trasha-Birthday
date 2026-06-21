"use client";

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

  // The tulip is clickable once unlocked and in the ready state.
  const canBeClicked = isUnlocked && state === "ready";

  return (
    <div
      ref={containerRef}
      className="relative flex flex-col items-center justify-center select-none"
      style={{
        zIndex: 30, // Elevated z-index to guarantee it sits above the background orbit paths
      }}
    >
      {/* Interactive overlay click target with clear bounds */}
      <div
        className={`absolute w-36 h-48 rounded-full z-40 transition-all duration-300 ${
          canBeClicked ? "cursor-pointer pointer-events-auto" : "pointer-events-none"
        }`}
        onClick={(e) => {
          if (canBeClicked) {
            e.stopPropagation();
            onClick();
          }
        }}
      />

      {/* Interactive Tooltip Glow indicator */}
      {canBeClicked && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: [0.5, 1, 0.5], y: 0 }}
          transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
          className="absolute -top-16 text-xs uppercase tracking-[0.25em] text-garden-glowPrimary text-center pointer-events-none text-shadow bg-black/60 px-4 py-1.5 rounded-full border border-garden-glowPrimary/20 backdrop-blur-sm whitespace-nowrap z-50"
        >
          Click flower to bloom
        </motion.div>
      )}

      {/* Crystal glow background behind the tulip */}
      <motion.div
        className="absolute w-52 h-52 rounded-full -z-10 pointer-events-none"
        style={{
          background: "radial-gradient(circle, rgba(255,179,209,0.35) 0%, rgba(255,214,231,0) 70%)",
        }}
        animate={{
          scale: canBeClicked ? [1, 1.15, 1] : [1, 1.05, 1],
          opacity: canBeClicked ? [0.7, 1, 0.7] : [0.4, 0.6, 0.4],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      {/* Premium Translucent Tulip SVG */}
      <motion.div
        className="sway-slow pointer-events-none"
        animate={{
          rotate: [0, -1.2, 0, 1.2, 0],
          y: [0, -3, 0, 3, 0],
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
          width="240"
          height="320"
          viewBox="0 0 200 300"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className={`filter drop-shadow-[0_0_15px_rgba(255,214,231,0.3)] transition-all duration-500 ${
            canBeClicked ? "hover:scale-105 active:scale-95 brightness-110" : "brightness-95"
          }`}
        >
          <defs>
            {/* Gradients */}
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

            {/* Glass shine masks */}
            <linearGradient id="shineGrad" x1="100" y1="60" x2="110" y2="200" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#ffffff" stopOpacity="0.8" />
              <stop offset="30%" stopColor="#ffffff" stopOpacity="0.1" />
              <stop offset="100%" stopColor="#ffd6e7" stopOpacity="0" />
            </linearGradient>
          </defs>

          {/* Stem */}
          <path
            d="M100,160 Q101,225 100,290"
            stroke="url(#stemGrad)"
            strokeWidth="5"
            strokeLinecap="round"
          />

          {/* Left Leaf */}
          <path
            d="M100,250 Q60,230 45,185 Q75,195 100,220 Z"
            fill="url(#leafGradLeft)"
            stroke="#43aa8b"
            strokeWidth="1"
            opacity="0.85"
          />

          {/* Right Leaf */}
          <path
            d="M100,235 Q140,215 155,170 Q125,180 100,205 Z"
            fill="url(#leafGradRight)"
            stroke="#43aa8b"
            strokeWidth="1"
            opacity="0.85"
          />

          {/* Base Calyx */}
          <path
            d="M90,165 Q100,172 110,165 Q105,152 95,152 Z"
            fill="#1e4d2b"
            opacity="0.9"
          />

          {/* Internal Glow Bulb (glowing Core) */}
          <circle
            cx="100"
            cy="125"
            r="24"
            fill="url(#petalGlowGrad)"
            filter="blur(8px)"
            opacity={canBeClicked ? 0.95 : 0.45 + bloomProgress * 0.55}
          />

          {/* CENTER INTIMATE INNER PETAL - rises during bloom */}
          <path
            d={`M100,65 Q85,110 82,145 Q100,160 118,145 Q115,110 100,65 Z`}
            fill="url(#petalGlowGrad)"
            stroke="#ffd6e7"
            strokeWidth="1.5"
            opacity="0.95"
            transform={`translate(0, ${-25 * bloomProgress}) scale(${1 + 0.15 * bloomProgress})`}
            style={{ transformOrigin: "100px 150px" }}
          />

          {/* LEFT INNER PETAL */}
          <path
            d="M100,75 Q75,100 70,140 Q90,152 100,140 Z"
            fill="url(#outerPetalGrad)"
            stroke="#ffb3d1"
            strokeWidth="1"
            opacity="0.8"
            transform={`rotate(${-35 * bloomProgress}, 100, 150)`}
            style={{ transformOrigin: "100px 150px" }}
          />

          {/* RIGHT INNER PETAL */}
          <path
            d="M100,75 Q125,100 130,140 Q110,152 100,140 Z"
            fill="url(#outerPetalGrad)"
            stroke="#ffb3d1"
            strokeWidth="1"
            opacity="0.8"
            transform={`rotate(${35 * bloomProgress}, 100, 150)`}
            style={{ transformOrigin: "100px 150px" }}
          />

          {/* LEFT OUTER MAIN PETAL */}
          <path
            d="M95,85 Q55,105 60,155 Q85,168 100,150 Z"
            fill="url(#outerPetalGrad)"
            stroke="#f7c8da"
            strokeWidth="1"
            opacity="0.85"
            transform={`rotate(${-48 * bloomProgress}, 100, 160)`}
            style={{ transformOrigin: "100px 160px" }}
          />

          {/* RIGHT OUTER MAIN PETAL */}
          <path
            d="M105,85 Q145,105 140,155 Q115,168 100,150 Z"
            fill="url(#outerPetalGrad)"
            stroke="#f7c8da"
            strokeWidth="1"
            opacity="0.85"
            transform={`rotate(${48 * bloomProgress}, 100, 160)`}
            style={{ transformOrigin: "100px 160px" }}
          />

          {/* Crystal shine lines overlaying the petals for a glass-like look */}
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
}