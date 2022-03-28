import React from "react";
import AlgoCard from "../AlgoCard";
import { Link } from "react-router-dom";
import styles from "./AlgorithmCards.module.scss";

export const AlgorithmCards = () => {
  return (
    <div className={styles.algoCardsContainer}>
      <Link to={{ pathname: `/algoOne` }}>
        <AlgoCard
          algoTitle="Algorithm 1"
          algoDescription="Lorem septum a bunch of other words and stuff."
        />
      </Link>
      <AlgoCard
        algoTitle="Algorithm 2"
        algoDescription="Lorem septum a bunch of other words and stuff."
      />
      <AlgoCard
        algoTitle="Algorithm 3"
        algoDescription="Lorem septum a bunch of other words and stuff."
      />
    </div>
  );
};

export default AlgorithmCards;
