import React from "react";
import styles from "./Header.module.scss";

export const Header = () => {
  return (
    <div className={styles.headerContainer}>
      <div className={styles.logo}>
        <h3>DS 402 Project</h3>
      </div>
      <div className={styles.navItems}>
        <h3>Algorithms</h3>
        <h3>About</h3>
      </div>
    </div>
  );
};

export default Header;
