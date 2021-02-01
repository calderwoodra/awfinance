import axios from "axios";
import {toastOnError} from "../../utils/Utils";
import {GET_LINK_TOKEN} from "./AccountsConnectTypes";

export const getLinkToken = () => dispatch => {
    axios
        .get("/api/v1/accounts/plaid/link_token/")
        .then(response => {
            dispatch({
                type: GET_LINK_TOKEN,
                payload: response.data
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};
