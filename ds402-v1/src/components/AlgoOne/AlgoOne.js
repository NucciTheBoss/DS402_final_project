import React, { useState } from "react";
import AddIcon from "@mui/icons-material/Add";
import Button from "@mui/material/Button";
import styles from "./AlgoOne.module.scss";
import TextField from "@mui/material/TextField";

export const AlgoOne = () => {
  const [members, setMembers] = useState([{ name: "", preferences: "" }]);

  const handleAddClicked = () => {
    setMembers([...members, { name: "", preferences: "" }]);
  };

  const handleRemoveClicked = (index) => {
    if (members.length > 1) {
      const membersTemp = [...members];
      membersTemp.splice(index, 1);
      setMembers(membersTemp);
    }
  };

  const handleNameChange = (index, newName) => {
    const membersTemp = [...members];
    membersTemp[index] = {
      name: newName,
      preferences: members[index].preferences,
    };
    setMembers(membersTemp);
  };

  const handleSubmit = () => {
    console.log(members);
  };

  return (
    <div>
      <div className={styles.toolBar}>
        <h4>Group Members</h4>
        <div className={styles.buttonContainer}>
          <AddIcon onClick={() => handleAddClicked()} />
        </div>

        <div className={styles.memberContainer}>
          <div className={styles.headerContainer}>
            <h4>Name</h4>
            <h4>Preferences</h4>
          </div>
          <div className={styles.members}>
            {members.map((member, index) => (
              <div key={index} className={styles.member}>
                <TextField
                  className={styles.nameField}
                  onInput={(name) => handleNameChange(index, name.target.value)}
                />
                <TextField />
                <Button
                  variant="contained"
                  color="error"
                  onClick={() => handleRemoveClicked(index)}
                >
                  Remove
                </Button>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className={styles.submitButtonContainer}>
        <Button onClick={() => handleSubmit()} variant="contained">
          Submit
        </Button>
      </div>
    </div>
  );
};

export default AlgoOne;
