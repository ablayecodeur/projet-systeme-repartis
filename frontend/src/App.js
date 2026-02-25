import React, { useEffect, useState } from "react";

function App() {
  const [produits, setProduits] = useState([]);

  useEffect(() => {
    fetch("http://192.168.49.2:32692/api/produits/")
      .then((response) => response.json())
      .then((data) => setProduits(data))
      .catch((error) => console.error("Erreur :", error));
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>Liste des Produits</h1>
      <ul>
        {produits.map((produit) => (
          <li key={produit.id}>
            <strong>{produit.nom}</strong> - {produit.prix} €
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;