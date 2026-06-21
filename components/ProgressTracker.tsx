"use client";

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
}