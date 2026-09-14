"use client";

import React, { useMemo } from "react";
import { motion } from "framer-motion";
import { useParallax } from "@/hooks/useParallax";

interface Star {
  id: number;
  x: number;
  y: number;
  size: number;
  delay: number;
  duration: number;
}

export function StarField() {
  const parallaxOffset = useParallax(15);

  const stars = useMemo(() => {
    const starList: Star[] = [];
    const seedRandom = (str: string) => {
      let hash = 0;
      for (let i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
      }
      return () => {
        const x = Math.sin(hash++) * 10000;
        return x - Math.floor(x);
      };
    };

    const rng = seedRandom("trasha-birthday-night-garden");

    for (let i = 0; i < 140; i++) {
      starList.push({
        id: i,
        x: rng() * 100,
        y: rng() * 100,
        size: rng() * 1.8 + 0.8,
        delay: rng() * 6,
        duration: rng() * 4 + 3,
      });
    }
    return starList;
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <motion.div
        className="relative w-full h-full"
        style={{
          x: parallaxOffset.x,
          y: parallaxOffset.y,
        }}
      >
        {stars.map((star) => (
          <motion.div
            key={star.id}
            className="absolute rounded-full bg-white"
            style={{
              left: `${star.x}%`,
              top: `${star.y}%`,
              width: star.size,
              height: star.size,
              boxShadow: star.size > 1.8 ? "0 0 6px #ffd6e7" : "none",
            }}
            animate={{
              opacity: [0.15, 0.95, 0.15],
              scale: [1, 1.25, 1],
            }}
            transition={{
              duration: star.duration,
              delay: star.delay,
              repeat: Infinity,
              ease: "easeInOut",
            }}
          />
        ))}
      </motion.div>
    </div>
  );
}