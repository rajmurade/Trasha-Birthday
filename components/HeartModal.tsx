"use client";

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
                Trasha's Dream Garden
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
}