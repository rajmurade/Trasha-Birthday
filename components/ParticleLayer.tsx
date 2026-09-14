"use client";

import React, { useMemo } from "react";
import { motion } from "framer-motion";
import { useParallax } from "@/hooks/useParallax";

interface DustParticle {
  id: number;
  startX: number;
  startY: number;
  endX: number;
  endY: number;
  size: number;
  duration: number;
  delay: number;
}

export function ParticleLayer() {
  const parallaxOffset = useParallax(35);

  const dustParticles = useMemo(() => {
    const list: DustParticle[] = [];
    const seedRandom = (str: string) => {
      let hash = 9831;
      for (let i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
      }
      return () => {
        const x = Math.sin(hash++) * 10000;
        return x - Math.floor(x);
      };
    };

    const rng = seedRandom("trasha-crystal-garden-dust");

    for (let i = 0; i < 45; i++) {
      const startX = rng() * 100;
      const startY = rng() * 100;
      const endX = startX + (rng() * 14 - 7);
      const endY = startY - (rng() * 20 + 5);

      list.push({
        id: i,
        startX,
        startY,
        endX,
        endY,
        size: rng() * 3 + 2,
        duration: rng() * 25 + 20,
        delay: rng() * -20,
      });
    }
    return list;
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <motion.div
        className="relative w-full h-full"
        style={{
          x: parallaxOffset.x * 1.5,
          y: parallaxOffset.y * 1.5,
        }}
      >
        {dustParticles.map((particle) => (
          <motion.div
            key={particle.id}
            className="absolute rounded-full"
            style={{
              background: "radial-gradient(circle, #ffd6e7 0%, rgba(255,179,209,0) 80%)",
              width: particle.size * 2,
              height: particle.size * 2,
              filter: "blur(0.5px)",
            }}
            initial={{
              x: `${particle.startX}%`,
              y: `${particle.startY}%`,
              opacity: 0,
            }}
            animate={{
              x: [`${particle.startX}%`, `${particle.endX}%`],
              y: [`${particle.startY}%`, `${particle.endY}%`],
              opacity: [0, 0.45, 0.75, 0.45, 0],
            }}
            transition={{
              duration: particle.duration,
              delay: particle.delay,
              repeat: Infinity,
              ease: "linear",
            }}
          />
        ))}
      </motion.div>
    </div>
  );
}