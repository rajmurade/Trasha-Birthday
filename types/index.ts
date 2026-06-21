export interface HeartItem {
  id: number;
  title: string;
  text: string;
}

export type BloomState = 
  | "ready" 
  | "blooming" 
  | "letter" 
  | "ending" 
  | "finished";

export interface Star {
  id: number;
  x: number;
  y: number;
  size: number;
  delay: number;
  duration: number;
}

export interface DustParticle {
  id: number;
  startX: number;
  startY: number;
  endX: number;
  endY: number;
  size: number;
  duration: number;
  delay: number;
}

export interface Petal {
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