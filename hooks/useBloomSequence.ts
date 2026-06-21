"use client";

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
}