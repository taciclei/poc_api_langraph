import React, { useEffect, useRef } from 'react';
import Split from 'split.js';

interface SplitPaneProps {
  left: React.ReactNode;
  right: React.ReactNode;
  direction?: 'horizontal' | 'vertical';
  sizes?: number[];
  minSize?: number;
}

export const SplitPane: React.FC<SplitPaneProps> = ({
  left,
  right,
  direction = 'horizontal',
  sizes = [50, 50],
  minSize = 100,
}) => {
  const splitRef = useRef<Split.Instance>();
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (containerRef.current) {
      splitRef.current = Split(containerRef.current.children as any, {
        sizes,
        minSize,
        direction,
        gutterSize: 4,
        cursor: direction === 'horizontal' ? 'col-resize' : 'row-resize',
      });
    }

    return () => {
      if (splitRef.current) {
        splitRef.current.destroy();
      }
    };
  }, [direction, JSON.stringify(sizes), minSize]);

  return (
    <div
      ref={containerRef}
      style={{
        display: 'flex',
        flexDirection: direction === 'horizontal' ? 'row' : 'column',
        height: '100%',
        width: '100%',
      }}
    >
      <div className="split-pane">{left}</div>
      <div className="split-pane">{right}</div>
    </div>
  );
};
