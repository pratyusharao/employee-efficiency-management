function deleteNote(noteId) {
    fetch("/", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/feedback";
    });
  }