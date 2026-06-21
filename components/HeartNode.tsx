"use client";

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
  // Compute fluid trigonometric coordinates around the central point
  const rad = (angle * Math.PI) / 180;
  const x = Math.cos(rad) * radius;
  const y = Math.sin(rad) * radius;

  return (
    <motion.div
      // We explicitly declare pointer-events-auto so that the node intercepts touch and click events
      // even though its parent layout container uses pointer-events-none.
      className="absolute z-20 cursor-pointer pointer-events-auto"
      style={{
        left: "50%",
        top: "50%",
      }}
      animate={{
        x: [x - 3, x + 3, x - 3],
        y: [y - 3, y + 3, y - 3],
      }}
      transition={{
        duration: 5 + (id % 2),
        repeat: Infinity,
        ease: "easeInOut",
      }}
      whileHover={{ scale: 1.15 }}
      whileTap={{ scale: 0.9 }}
      onClick={(e) => {
        e.preventDefault();
        e.stopPropagation();
        onClick();
      }}
    >
      {/* Centering translate wrapper */}
      <div className="relative -left-1/2 -top-1/2 flex flex-col items-center">
        {/* The tactile heart glass button */}
        <div
          className={`w-12 h-12 sm:w-14 sm:h-14 rounded-full flex items-center justify-center transition-all duration-300 relative ${
            isOpened
              ? "glass-button border-garden-glowPrimary shadow-[0_0_20px_rgba(255,214,231,0.5)] text-garden-glowPrimary bg-garden-glowPrimary/10"
              : "glass-panel text-garden-accent hover:border-garden-glowSecondary hover:text-garden-glowSecondary active:bg-white/10"
          }`}
        >
          {isOpened ? (
            <Sparkles className="w-4 h-4 sm:w-5 sm:h-5 animate-pulse" />
          ) : (
            <Heart className="w-4 h-4 sm:w-5 sm:h-5 fill-current opacity-70" />
          )}

          {/* Glowing indicator light */}
          <span className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-garden-glowPrimary shadow-[0_0_8px_#ffd6e7]" />
        </div>

        {/* Dynamic Label */}
        <span className="mt-1.5 text-[8px] sm:text-[10px] tracking-[0.15em] uppercase text-garden-text/90 whitespace-nowrap bg-garden-bg/95 px-2 py-0.5 rounded-full border border-white/10 font-serif">
          {title}
        </span>
      </div>
    </motion.div>
  );
}