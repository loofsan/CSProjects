import { useState } from "react";
import Playlist from "../components/Playlist";
import Header from "../components/Header";
import Footer from "../components/Footer";
import "./App.css";

// define an array of initial movies
const initialPlaylist = [
  {
    id: 1,
    title: "Espresso",
    artist: "Sabrina Carpenter",
    year: 2024,
    favorite: false,
  },
  {
    id: 2,
    title: "Electric Feel",
    artist: "MGMT",
    year: 2007,
    favorite: false,
  },
  {
    id: 3,
    title: "Come As You Are",
    artist: "Nirvana",
    year: 1991,
    favorite: false,
  },
  {
    id: 4,
    title: "Dancing Queen",
    artist: "ABBA",
    year: 1976,
    favorite: true,
  },
];

const App = () => {
  const [playlist] = useState(initialPlaylist);

  return (
    <>
      <Header appName="My Playlist" />

      <main className="main-content">
        <Playlist songs={playlist} />
      </main>

      <Footer appName="My Playlist" />
    </>
  );
};

export default App;
