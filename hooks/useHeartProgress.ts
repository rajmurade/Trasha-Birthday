"use client";

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
}