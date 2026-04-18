import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('App', () => {
  test('renders App component', () => {
    render(<App />);
    const appElement = screen.getByText(/Edit/i);
    expect(appElement).toBeInTheDocument();
  });

  test('renders logo', () => {
    render(<App />);
    const logoElement = screen.getByAltText(/logo/i);
    expect(logoElement).toBeInTheDocument();
  });

  test('renders learn react link', () => {
    render(<App />);
    const linkElement = screen.getByText(/Learn React/i);
    expect(linkElement).toBeInTheDocument();
  });

  test('link has correct href', () => {
    render(<App />);
    const linkElement = screen.getByText(/Learn React/i);
    expect(linkElement).toHaveAttribute('href', 'https://reactjs.org');
  });
});