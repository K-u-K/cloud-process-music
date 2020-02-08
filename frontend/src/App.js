import React from 'react';

function App() {
  return (
    <div>
      <main className="container">
        <div className="pt-5">
          <h1 className="display">🎵 Process Music 🎶</h1>
          <p className="lead">
            Process your musical composition provided as MIDI file
          </p>
        </div>
        <hr/>
        <div className="pt-5">
          <h3 className="display">Explanation</h3>
          <p>
            Process Music generates other representation of your musical composition
            by parsing and evaluating the binary format which represents the MIDI format.
            Each instruction, each note event will be converted into a specific log-like
            format which allows further analysis and dissection of the musical components
            the composition is made of. 🎻 
          </p>
          <p>
            By uploading your MIDI file, you will receive a zipped archive containing
            multiple files which all contribute to a general analysis of your composition
          </p>
          <div className="pt-2">
            <ul className="list-group">
              <li className="list-group-item">
                <strong>CSV</strong> - a comma seperated file which lists all musical event sequentually
              </li>
              <li className="list-group-item">
                <strong>XES</strong> - eXtensible Event Stream, a XML-based file format 
                with which further and deep-diving analysis of the composition is made possible
              </li>
              <li className="list-group-item">
                <strong>Footprint Matrix</strong> - a grid which contains all octave-agnostric notes of the chromatic scales
                where an element in the matrix marks whether the note is followed, follows another musical note
                or both
              </li>
            </ul>
          </div>
        </div>
        <div className="pt-5">
          <h3 className="display">Upload the MIDI file</h3>
          <form action="http://localhost:5000/upload" method="post" enctype="multipart/form-data">
            <div>
              <span>
                <input type="file" name="file"/>
              </span>
              <span className="pl-3">
                <button type="submit" className="btn btn-primary">Submit your upload</button>
              </span>
            </div>
          </form>
        </div>
      </main>
      <footer className="footer">
        <div className="container p-5">
          <div className="row" style={{fontSize: "20px"}}>
            <div className="col">
              <strong>Built</strong> with love and music 🎷 by Patrick Keller &amp; Alen Kocaj
            </div>
            <div className="col">
              <strong>Find</strong> or <strong>contribute</strong> to the the project on <a href="https://github.com/K-u-K/process-music" target="blank">Github</a>
            </div>
            <div className="col">
              <strong>Copyright ©</strong> 2020 by <a href="https://github.com/K-u-K" target="blank">K&amp;K</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
