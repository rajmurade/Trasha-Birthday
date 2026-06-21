"use client";

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
}