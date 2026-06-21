"use client";

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

  // Derive display controls
  const isMainInterfaceVisible = bloomState === "ready" || bloomState === "blooming";

  return (
    <main className="relative w-screen h-screen overflow-hidden flex flex-col items-center justify-between p-6 sm:p-8">
      <BackgroundScene />

      {/* Consent Intro Overlay */}
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

      {/* Main Interactive Screen components (We keep them mounted but fade out gracefully during blooming/letter states) */}
      {hasInteracted && (
        <motion.div
          className="absolute inset-0 w-full h-full flex flex-col items-center justify-between p-6 sm:p-8"
          initial={{ opacity: 1 }}
          animate={{ 
            opacity: isMainInterfaceVisible ? 1 : 0,
            pointerEvents: bloomState === "ready" ? "auto" : "none"
          }}
          transition={{ duration: 1.5, ease: "easeInOut" }}
        >
          {/* Top Header */}
          <header className="w-full flex flex-col items-center text-center mt-4 pointer-events-none z-10">
            <h1 className="text-2xl sm:text-3xl font-serif text-white tracking-wide font-medium leading-normal text-glow">
              Samiksha's Garden
            </h1>
            <p className="text-[10px] tracking-[0.22em] uppercase text-garden-accent/70 mt-1">
              Reveal the secret stars to find her flower
            </p>
          </header>

          {/* Central Interactive area */}
          <div className="relative w-full h-[55vh] flex items-center justify-center">
            {/* Orbit layer */}
            <HeartOrbit
              hearts={HEARTS_DATA}
              openedHearts={openedHearts}
              onOpenNode={handleOpenNode}
            />

            {/* Centered Tulip layer */}
            <CrystalTulip
              isUnlocked={isUnlocked}
              bloomProgress={bloomProgress}
              onClick={startBloom}
              state={bloomState}
            />
          </div>

          {/* Progress Tracker Footer */}
          <div className="mb-6 z-20">
            <ProgressTracker
              openedCount={openedHearts.length}
              totalCount={HEARTS_DATA.length}
              isUnlocked={isUnlocked}
            />
          </div>
        </motion.div>
      )}

      {/* Secrets Modal */}
      <HeartModal
        isOpen={activeModal.isOpen}
        onClose={handleCloseModal}
        title={activeModal.title}
        text={activeModal.text}
      />

      {/* Cinematic Timeline GSAP Bloom Controller */}
      <BloomController
        isActive={bloomState === "blooming"}
        onTimelineProgress={(val) => setBloomProgress(val)}
        onComplete={revealLetter}
      />

      {/* Final Glass Letter panel */}
      <AnimatePresence>
        {bloomState === "letter" && (
          <LetterReveal
            onClose={() => {
              startEnding();
            }}
          />
        )}
      </AnimatePresence>

      {/* Audio player */}
      {hasInteracted && <AudioManager audioState={audioState} />}

      {/* Glass petal falling rain */}
      {(bloomState === "ending" || bloomState === "finished" || bloomState === "letter") && (
        <PetalRain />
      )}

      {/* Final sequence */}
      {bloomState === "ending" && <EndingSequence />}
    </main>
  );
}