"use client";

import React, { useState, useEffect } from "react";
import { HeartNode } from "./HeartNode";

interface HeartItem {
  id: number;
  title: string;
  text: string;
}

interface HeartOrbitProps {
  hearts: HeartItem[];
  openedHearts: number[];
  onOpenNode: (id: number, title: string, text: string) => void;
}

export function HeartOrbit({ hearts, openedHearts, onOpenNode }: HeartOrbitProps) {
  const [radius, setRadius] = useState(135);

  useEffect(() => {
    if (typeof window === "undefined") return;

    const handleResize = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;

      // Calculate a highly fluid, responsive radius that fits any screen size comfortably
      if (width < 380 || height < 600) {
        setRadius(85); // Ultra-compact for small phones or landscape mode
      } else if (width < 640) {
        setRadius(105); // Ergonomic spacing for standard mobile devices
      } else if (width < 1024) {
        setRadius(135); // Spacious for tablets
      } else {
        setRadius(165); // Full display grandeur for desktops and larger screens
      }
    };

    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none z-10 flex items-center justify-center">
      {/* Background dashed orbit guide line */}
      <div
        className="absolute rounded-full border border-dashed border-garden-glowPrimary/10 pointer-events-none transition-all duration-300"
        style={{
          width: radius * 2,
          height: radius * 2,
        }}
      />

      {hearts.map((heart, index) => {
        // Distribute the hearts evenly
        const angle = (360 / hearts.length) * index - 90;
        const isOpened = openedHearts.includes(heart.id);

        return (
          <HeartNode
            key={heart.id}
            id={heart.id}
            title={heart.title}
            angle={angle}
            radius={radius}
            isOpened={isOpened}
            onClick={() => onOpenNode(heart.id, heart.title, heart.text)}
          />
        );
      })}
    </div>
  );
}