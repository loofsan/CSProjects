import { useState } from "react";
import "./PlayList.css";

const Playlist = ({ songs }) => {
  const [activeId, setActiveId] = useState(null);

  return (
    <div className="play-list">
      <ul>
        {songs.length === 0 ? (
          <li>There are no songs.</li>
        ) : (
          songs.map((song) => (
            <li
              key={song.id}
              className={activeId === song.id ? "active" : ""}
              onClick={() => setActiveId(song.id)}
            >
              {song.title} by {song.artist} ({song.year}){song.favorite && "★"}
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

export default Playlist;
