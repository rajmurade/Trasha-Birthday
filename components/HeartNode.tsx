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
}