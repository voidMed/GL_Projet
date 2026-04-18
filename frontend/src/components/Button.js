import React from 'react';

export function Button({ onClick, children, disabled = false }) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
}