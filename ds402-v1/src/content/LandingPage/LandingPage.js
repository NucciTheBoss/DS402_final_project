import React from "react";
import AlgorithmCards from "../../components/AlgorithmCards";
import styles from "./LandingPage.module.scss";
export const LandingPage = () => {
  return (
    <div>
      <div className={styles.cardsContainer}>
        <AlgorithmCards />
      </div>
    </div>
  );
};

export default LandingPage;
