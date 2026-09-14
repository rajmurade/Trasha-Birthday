"use client";

import React, { useEffect, useRef } from "react";

interface Petal {
  x: number;
  y: number;
  r: number;
  d: number;
  opacity: number;
  rotation: number;
  rotationSpeed: number;
  horizontalSpeed: number;
  verticalSpeed: number;
}

export function PetalRain() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrameId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };
    window.addEventListener("resize", handleResize);

    const petals: Petal[] = [];
    const maxPetals = 85;

    for (let i = 0; i < maxPetals; i++) {
      petals.push({
        x: Math.random() * width,
        y: Math.random() * height - height,
        r: Math.random() * 8 + 6,
        d: Math.random() + 0.5,
        opacity: Math.random() * 0.6 + 0.35,
        rotation: Math.random() * 360,
        rotationSpeed: Math.random() * 1.5 - 0.75,
        horizontalSpeed: Math.random() * 1.5 - 0.75,
        verticalSpeed: Math.random() * 1.5 + 1.0,
      });
    }

    const drawPetal = (
      ctx: CanvasRenderingContext2D,
      x: number,
      y: number,
      r: number,
      rotation: number,
      opacity: number
    ) => {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate((rotation * Math.PI) / 180);
      ctx.beginPath();

      ctx.moveTo(0, 0);
      ctx.quadraticCurveTo(-r / 1.5, -r / 1.5, -r, 0);
      ctx.quadraticCurveTo(-r / 1.5, r / 1.5, 0, r);
      ctx.quadraticCurveTo(r / 1.5, r / 1.5, r, 0);
      ctx.quadraticCurveTo(r / 1.5, -r / 1.5, 0, 0);

      const gradient = ctx.createLinearGradient(-r, -r, r, r);
      gradient.addColorStop(0, `rgba(255, 214, 231, ${opacity})`);
      gradient.addColorStop(0.5, `rgba(255, 179, 210, ${opacity * 0.85})`);
      gradient.addColorStop(1, `rgba(247, 200, 218, ${opacity * 0.5})`);

      ctx.fillStyle = gradient;
      ctx.fill();

      ctx.strokeStyle = `rgba(255, 255, 255, ${opacity * 0.3})`;
      ctx.lineWidth = 0.5;
      ctx.stroke();

      ctx.restore();
    };

    const update = () => {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < maxPetals; i++) {
        const petal = petals[i];
        petal.y += petal.verticalSpeed;
        petal.x += petal.horizontalSpeed + Math.sin(petal.y / 30) * 0.5;
        petal.rotation += petal.rotationSpeed;

        if (petal.y > height + 20) {
          petal.y = -20;
          petal.x = Math.random() * width;
          petal.verticalSpeed = Math.random() * 1.5 + 1.0;
          petal.horizontalSpeed = Math.random() * 1.5 - 0.75;
        }

        if (petal.x > width + 20) {
          petal.x = -20;
        } else if (petal.x < -20) {
          petal.x = width + 20;
        }

        drawPetal(ctx, petal.x, petal.y, petal.r, petal.rotation, petal.opacity);
      }

      animationFrameId = requestAnimationFrame(update);
    };

    update();

    return () => {
      window.removeEventListener("resize", handleResize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return <canvas ref={canvasRef} className="fixed inset-0 pointer-events-none z-30" />;
}