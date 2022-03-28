import React from "react";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import styles from "./AlgoOne.module.scss";
import TextField from "@mui/material/TextField";

export const AlgoOne = () => {
  return (
    <div>
      <div className={styles.toolBar}>
        <h4>Group Members</h4>
        <div className={styles.buttonContainer}>
          <RemoveIcon />
          <AddIcon />
        </div>

        <div className={styles.memberContainer}>
          <div className={styles.headerContainer}>
            <h4>Name</h4>
            <h4>Preferences</h4>
          </div>
          <div className={styles.member}>
            <TextField />
            <TextField />
          </div>
        </div>
      </div>
    </div>
  );
};

export default AlgoOne;
