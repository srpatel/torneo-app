<script>
  import { onMount } from "svelte";
  import { push } from "svelte-spa-router";
  import apiCall from "utils/api-call.js";

  export let params;

  let tournament = null;

  onMount(async () => {
    // Load tournament list from db
    if (params?.code) {
        const response = await apiCall("tournament/" + params.code);
        if (response.isSuccess) {
            tournament = response.data;
        }
    }
  });

  let deleting = false;
  let error = null;

  async function handleDelete() {
    deleting = true;
    try {
      const { data, isSuccess } = await apiCall("tournament/" + tournament.code, null, "DELETE");
      if (isSuccess) {
        push("/");
      } else {
        error = data.detail;
      }
    } catch (e) {
      console.error(e);
    }
    deleting = false;
  }
</script>


{#if tournament}

<div class="card bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title">{tournament.name}</h2>
    <p>Id: {tournament.id}</p>
    <p>Code: {tournament.code}</p>
    <p>Created at: {tournament.created_at}</p>
    <div class="card-actions justify-end">
      <button class="btn" on:click={handleDelete} disabled={deleting}>Delete</button>
    </div>
  </div>
</div>

{/if}