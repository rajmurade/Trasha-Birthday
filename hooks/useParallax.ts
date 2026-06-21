"use client";

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
}